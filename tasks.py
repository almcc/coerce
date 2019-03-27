from invoke import task


@task
def clean(ctx):
    ctx.run("rm -rf dist")


@task
def build(ctx):
    ctx.run("python setup.py sdist")


@task
def publish_test(ctx):
    ctx.run("twine upload -r testpypi dist/*.tar.gz")


@task
def publish_public(ctx):
    ctx.run("twine upload dist/*.tar.gz")
