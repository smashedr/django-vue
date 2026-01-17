import logging
import os

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


log = logging.getLogger("app")
cache_seconds = 60 * 60 * 4


@csrf_exempt
def index_view(request, path=None):
    """
    View  /
    """
    log.debug("home_view: %s - %s", request.method, request.META["PATH_INFO"])
    log.debug("path: %s", path)

    # log.debug("---- request.META ----")
    # log.debug(request.META)

    log.debug("---- request.headers ----")
    log.debug(request.headers)

    log.debug("---- request.body ----")
    log.debug(request.body)

    log.debug("DEBUG: %s", os.environ.get("DEBUG"))

    # return HttpResponse(path)
    return JsonResponse(dict(request.headers), json_dumps_params={"indent": 2})
