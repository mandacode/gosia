import logging

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .services import get_works

logger = logging.getLogger(__name__)

# TODO FLOW: create works -> create scratchpad -> update scratchpad -> create bill -> print bill


@login_required
def dashboard_view(request):

    works = get_works()

    return render(request, 'works/dashboard.html', {'works': works})
