[![Workflow Lint](https://img.shields.io/github/actions/workflow/status/smashedr/django-vue/lint.yaml?logo=verizon&label=lint)](https://github.com/smashedr/django-vue/actions/workflows/lint.yaml)
[![GitHub Last Commit](https://img.shields.io/github/last-commit/smashedr/django-vue?logo=speedtest&label=updated)](https://github.com/smashedr/django-vue)
[![GitHub Repo Size](https://img.shields.io/github/repo-size/smashedr/django-vue?logo=buffer&label=repo%20size)](https://github.com/smashedr/django-vue?tab=readme-ov-file#readme)
[![GitHub Top Language](https://img.shields.io/github/languages/top/smashedr/django-vue?logo=devbox)](https://github.com/smashedr/django-vue?tab=readme-ov-file#readme)
[![GitHub Contributors](https://img.shields.io/github/contributors-anon/smashedr/django-vue?logo=southwestairlines)](https://github.com/smashedr/django-vue/graphs/contributors)
[![GitHub Issues](https://img.shields.io/github/issues/smashedr/django-vue?logo=codeforces&logoColor=white)](https://github.com/smashedr/django-vue/issues)
[![GitHub Discussions](https://img.shields.io/github/discussions/smashedr/django-vue?logo=rocketdotchat&logoColor=white)](https://github.com/smashedr/django-vue/discussions)
[![GitHub Forks](https://img.shields.io/github/forks/smashedr/django-vue?style=flat&logo=forgejo&logoColor=white)](https://github.com/smashedr/django-vue/forks)
[![GitHub Repo Stars](https://img.shields.io/github/stars/smashedr/django-vue?style=flat&logo=gleam&logoColor=white)](https://github.com/smashedr/django-vue/stargazers)
[![GitHub Org Stars](https://img.shields.io/github/stars/cssnr?style=flat&logo=apachespark&logoColor=white&label=org%20stars)](https://cssnr.github.io/)
[![Discord](https://img.shields.io/discord/899171661457293343?logo=discord&logoColor=white&label=discord&color=7289da)](https://discord.gg/wXy6m2X8wY)
[![Ko-fi](https://img.shields.io/badge/Ko--fi-72a5f2?logo=kofi&label=support)](https://ko-fi.com/cssnr)

# Django Vue

Django Vue Docker Project.

Work in Progress...

## Development

Requirements:

- [Docker](https://docs.docker.com/engine/install/) - For Docker Stack
- [Node](https://nodejs.org/en/download) - For Vite dev
- [UV](https://docs.astral.sh/uv/getting-started/installation/) - For Django runserver

The fastest way to get started is with Docker using the [docker-compose.yaml](docker-compose.yaml).

```shell
docker compose up --watch --build
```

Then visit: http://localhost/

### Project

| Folder          | Description                                            |
| --------------- | ------------------------------------------------------ |
| [app](#app)     | Backend - Django Application                           |
| [web](#web)     | Frontend - Vue + Vite Application                      |
| [nginx](#nginx) | Webserver - Builds [web](#web) and Proxies [app](#app) |

You can also run the web (Vite+Vue) and backend (Django) separately.

This is the only way to make full use of the Vite Dev tools.

To do this, start the [App](#app) in one terminal and the [Web](#web) in another.

#### App

- [app/Dockerfile](app/Dockerfile)

```shell
cd app
uv sync
run dev
```

Then visit: http://localhost:9000/

#### Web

- [web/Dockerfile](web/Dockerfile)

```shell
cd web
npm install
npm run dev
```

Then visit: http://localhost:5173/

Tip: You can optionally set the `DJANGO_HOST` environment variable.

#### Nginx

- [nginx/Dockerfile](nginx/Dockerfile)

This container is used in production in place of [Web](#web).

See the [docker-compose-stack.yaml](docker-compose-stack.yaml) for more details.
