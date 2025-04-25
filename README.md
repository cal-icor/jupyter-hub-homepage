# Custom JupyterHub template for [CAL-ICOR Jupyterhubs](https://https://base.jupyter.cal-icor.org/)

This repo contains html jinja2 templates for customising the appearance of JupyterHub. Each HTML file here will override the files in `https://github.com/jupyterhub/jupyterhub/tree/master/share/jupyter/hub/templates`.

<!-- Any changes made in this repository will be reflected in the JupyterHub within 5 minutes. -->

## Local development

You can run a local JupyterHub to test your template changes.

1. Setup a virtual python environment and ensure you have NPM installed.

2. Set up [`configurable-http-proxy`](https://github.com/jupyterhub/configurable-http-proxy#install)

3. Install packages from `requirements.txt`

   ```bash
   python3 -m pip install -r requirements.txt
   ```

4. Symlink extra assets we have, so templates can use it.

   ```bash
   ln -s $(pwd)/extra-assets $(dirname $(which python3))/../share/jupyterhub/static
   ```

5. Add extra templates variables you might use in the templates, by editing
   `jupyterhub_config.py` file's `c.JupyterHub.template_vars`

6. Start a JupyterHub!

   ```bash
   python3 -m jupyterhub
   ```

7. Check out your work at `http://localhost:8000`.

8. If you change templates, you need to restart JupyterHub to see changes.
   But for asset changes (JS, CSS, etc) you don't need a restart
