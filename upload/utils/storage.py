from django.conf import settings


def ext3_shard(uid):
    """ext3 subfolders limit workaround"""
    return int(uid) // (32000-2)


def img_url(n, uid):
    folder = settings.MEDIA_URL+'tmp'
    if uid:
        folder = settings.MEDIA_URL+'%s/%s' % (ext3_shard(uid), uid)
    if n != None:
        return folder + '/%s.jpg' % n
    return ''


def img_path(n, uid):
    if n != None:
        return settings.STATIC_ROOT + img_url(n, uid)
    return ''