# Utils for tasks

def upload_filename(instance, filename):
    return f"attachments/{instance.task.user.email}/{filename}"