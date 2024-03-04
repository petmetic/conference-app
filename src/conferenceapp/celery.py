from celery import Celery

app = Celery(
    "conferenceapp",
    broker="redis://",
    backend="rpc://",
    include=["conferenceapp.tasks"],
)

# # Optional configuration, see the application user guide.
# app.conf.update(
#     result_expires=3600,
# )

if __name__ == "__main__":
    app.start()
