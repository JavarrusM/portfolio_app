from django.shortcuts import render, get_object_or_404
from .models import Analysis


def all_analyses(request):
    analyses = Analysis.objects.order_by('-date')
    return render(request, 'analysis/all_analyses.html', {'analyses': analyses})


def detail(request, analysis_id):
    analysis = get_object_or_404(Analysis, pk=analysis_id)
    return render(request, 'analysis/detail.html', {'id': analysis_id, 'analysis': analysis})
