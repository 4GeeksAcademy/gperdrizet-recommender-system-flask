# ML web app with Flask: movie recommendation engine

**Note**: Render 'scales to zero', so it may take a few minutes for the service to start back up if no one has used it in a while.


## 1. Introduction

This repository contains a minimal public web application deployment of the movie recommendation model we built earlier in the course.

The project consists of four components:

1. **[Recommender function](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-flask/blob/main/notebooks/solution.ipynb)**: This Python function is the heart of the app. It takes a movie title and uses a k-nearest neighbors and a movie database to return recommendations of other similar movies.
2. **[Flask](https://flask.palletsprojects.com/en/stable/)**: Flask is a simple web application framework, it will act as the go-between to bridge the html world of the user's web-browser and our internal python function.
3. **[Gunicorn](https://gunicorn.org/)**: Gunicorn is the web server that will serve the page to users and send data to our application via Flask.
4. **[Render](https://render.com/)**: Render is the cloud hosting service we will use to actually run our application. This allows the app to have a public URL where it can be accessed by users.


## 2. Local testing

To test your app locally inside your codespace run the following command in the terminal:

```bash
gunicorn src.movie_recommender:app
```

This will allow you to test the app out, without having to actually deploy it to Render and will save you a lot of time. Once everything is working, it's time to deploy.


## 3. Render deployment

Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and are finally taken to the [Render Dashboard](https://dashboard.render.com/). From there, we can create a new service for our application:

1. Click '+ New' button at the top right and select 'Web Service' from the dropdown menu
2. Select 'Public Git Repository' and paste the link to your project repository
3. Click 'Connect'

This will take you to the new web service dashboard. Then, from the settings tab set the following values:

1. **Name**: whatever you want
2. **Project**: don't need to add to a project - this is generally for more complex deployments that comprise multiple services
3. **Language**: Python 3
4. **Branch**: main
5. **Region**: Ohio (US east) - or whatever is closest to you
6. **Root directory**: don't set
7. **Build Command**: pip install deployment_requirements.txt
8. **Start Command**: gunicorn src.movie_recommender:app

Under 'Advanced' set autodeploy to 'off'.

After that, set the instance type to free, and you can leave everything else alone. Click 'Deploy Web Service'! You should see the setup.sh script being run in the log terminal. If there were no problems, you can now access your web app at the URL provided at the top of the page, under the project name and GitHub repository link.


## 4. CI/CD and GitHub Workflows (optional)

This repository also demonstrates a simple CI/CD workflow for automated testing and deployment of a ML app to Render using pytest and GitHub workflows. It should be easily adaptable to other simple Render deployments. The rest of this README documents the set-up steps.


### Outline

1. Workflow 
2. Parts list
2. The movie recommender app
3. pytest automation with GitHub workflows
4. Automatic deployment with GitHub workflows
6. Render deployment target set up
7. Authentication
8. How to get those cool 'passing' badges
9. How to start the app automatically in codespaces


### 4.1. Workflow

1. A developer on the project submits a pull request containing updates to the main fork.
2. The automated tests runs & the results are displayed in the pull request.
2. A human being sanity checks the changes and merges or closes the pull request at their discretion (this is the last human in the loop step!).
3. Merging the pull request triggers the deployment workflow.
4. The new version of the app is sent to Render.
5. Render spins up the new version of the app.


### 4.2. Parts list

1. **GitHub**: hosts the code and orchestrates the pipeline.
2. **GitHub Codespaces**: used to develop and train the model and build the app.
3. **Pytest**: tests code for basic functionality before deploying.
4. **GitHub workflows**: orchestrates the testing and deployment of the app.
5. **GitHub actions**: does the deployment.
6. **Render**: hosts the app.


### 4.3. The movie recommender app

The only major difference in the app itself is the addition of testing with [pytest](https://docs.pytest.org/en/stable/index.html). Testing is needed since deployment will be automated - we don't want to deploy broken code and bring down the app!

The example repository contains [one simple test](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-flask/blob/main/tests/test_model.py) to check the model's output against a known case:

```python
import movie_recommender.movie_recommender as recommender

def test_model_output():
    '''Tests to see if the model is giving sane output.'''

    # Call then recommendation function with an input for which we know the expected output
    similar_movies=recommender.get_movie_recommendations(
        'Star Wars',
        recommender.MODEL,
        recommender.TFIDF_MATRIX,
        recommender.TAG_TITLE_DF
    )

    # Check that we received the expected answer
    assert similar_movies[0] == 'The Empire Strikes Back'
```

The test can be run inside of a Codespace from the testing tab of the activities bar or via the command line with:

```bash
python -m pytest tests/test_model.py
```


### 4.4. Pytest automation with GitHub workflows

Next, we will set-up this test to run automatically when a pull request is created on main using [GitHub Workflows](https://docs.github.com/en/actions/use-cases-and-examples/building-and-testing/building-and-testing-python). This ensures that we don't merge bad code to main and deploy it to production. In reality you would want more than just this one simple test, but it servers to demonstrate the workflow.

Follow the instructions above to generate a workflow template for building and testing Python. You only need to follow the section *Using a Python workflow template*, the rest is more than we need. Here is what the build/test [workflow file](https://github.com/4GeeksAcademy/gperdrizet-recommender-system-flask/blob/main/.github/workflows/pytest.yml) looks like:

```yaml
# This workflow will install Python dependencies and run tests

name: Pytest

on:
  pull_request:
    branches: [ "main" ]

permissions:
  contents: read

jobs:
  test:
    name: Test with Python 3.11
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    - name: Set up Python 3.11
      uses: actions/setup-python@v5
      with:
        python-version: "3.11"
        cache: "pip"
        
    - name: Install dependencies
      run: |
        python -m pip install -r deployment_requirements.txt

    - name: Test with pytest
      run: python -m pytest tests/test_model.py
```

This workflow will set-up a Python 3.11 build environment, install the project dependencies and then run the test(s). Next, we will add a step to deploy to Render. You can also use a branch protection rule to **require** that this test passes before pull requests are merged to main. See instructions [here](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/managing-a-branch-protection-rule).


### 4.5. Automatic deployment with GitHub workflows

For Render deployment, we will use the GitHub action [Deploy to Render](https://github.com/gperdrizet/render-deploy). **Note**: this action is a community contribution - for long term deployment or major projects you would probably want to fork and maintain your own clone. This file points to my fork of it, so if you trust that I won't break or delete it, you're all set (I won't - I use it too). Here is the full workflow file:

```yaml
name: Render deployment

on:
  push:
    branches: [ "main" ]

  workflow_dispatch:

permissions:
  contents: read

jobs:
    deploy:
        name: 'Deploy to Render'
        runs-on: ubuntu-latest

        permissions:
            deployments: write

        steps:
          - uses: gperdrizet/render-deploy@1.0.0
            with:
              service_id: ${{ secrets.RENDER_SERVICE_ID }}
              api_key: ${{ secrets.RENDER_API_KEY }}
              wait_deploy: true
              github_deployment: true
              deployment_environment: 'production'
              github_token: ${{ secrets.GITHUB_TOKEN }}
```

Don't change the `RENDER_SERVICE_ID`, `RENDER_SERVICE_ID` or `GITHUB_TOKEN`. These are environment variables which will be populated from GitHub secrets at runtime.


### 4.6. Set-up Render target

Now, we need to set-up a Render service to deploy to. This will only need to be done once, after that, the GitHub workflow will check and deploy new pull requests for us.

Go to [render.com](https://render.com/) and click 'Get started for free'. The site will ask for an email address and password and then send you a conformation link. After clicking the link, you are asked to fill out some basic profile details and are finally taken to the Render Dashboard. From there, we can create a new service for our application:

1. Click '+ New' button at the top right and select 'Web Service' from the dropdown menu
2. Select 'Public Git Repository' and paste the link to your project repository
3. Click 'Connect'

This will take you to the new web service dashboard. Then, from the settings tab set the following values:

- **Name**: whatever you want
- **Project**: don't need to add to a project - this is generally for more complex deployment that comprise multiple services
- **Language**: Python 3
- **Branch**: main
- **Region**: Ohio (US east) - or whatever is closest to you
- **Root directory**: don't set - will default to the project root
- **Build Command**: `pip install -r deployment_requirements.txt`
- **Start Command**: `gunicorn src.movie_recommender:app`
- **Instance type**: Free

Lastly, under the 'Advanced' drop-down menu at the bottom of the page, make sure to turn automatic deployment off. We will manage deployment from GitHub and don't want Render to try and re-deploy every new commit. Then click 'Deploy'. Your web app should spin up after a few minutes. Congrats, the app works!


### 4.7. Authentication

Last bit of set-up is to store your Render credentials on GitHub so that the GitHub workflow can deploy to Render on your behalf. To do this, we will use GitHub's [secrets](https://docs.github.com/en/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions). Follow the instructions to add:

1. RENDER_SERVICE_ID (found in the URL of the service page on Render)
2. RENDER_API_KEY (Go to your Render profile > account settings > API keys)


### 4.8. How to get those cool 'passing' badges

From the GitHub 'Actions' tab:

1. Click on a run of the workflow you want a badge for.
2. Click on the three dot menu next to 'Re-run all jobs' at the upper right.
3. Choose 'Create status badge'.
4. Copy the markdown to your README file.


### 4.9. How to start the app automatically in codespaces

Codespaces run an instance of the development container specified by `.devcontainer/container.json`. You can set-up lots of fun stuff from there. To start the app on an internal Gunicorn server use the following:

```json
"postAttachCommand": "gunicorn src.movie_recommender:app"
```

This will start the app whenever a codespace is opened on the repository.