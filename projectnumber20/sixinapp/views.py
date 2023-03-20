from .models import Musician, Album
from django.views.generic import ListView,DetailView


class MusicianListView(ListView):
    model1=Musician
    template_name="musician_list.html"
    paginate_by=1


class AlbumDetailView(DetailView):
    model2=Album
    model2.objects.filter(num_stars__gte=3)
    template_name='album_detail.html'
    
