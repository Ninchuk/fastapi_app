from conf.config import settings

bind = f"{settings.BIND_IP}:{settings.BIND_PORT}"
worker_class = "uvicorn.workers.UvicornWorker"
workers = settings.WEB_CONCURRENCY
proc_name = "web"
wsgi_app = "webapp.main:app"
