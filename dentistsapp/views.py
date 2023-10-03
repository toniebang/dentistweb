from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, Doctores, Mensaje, Cita, Categoria, Comentario
from .forms import MessageForm, ApointmentForm, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    posts = Post.objects.all().order_by('-fecha_publicacion')
    doctores = Doctores.objects.all()
    apointment = Cita.objects.all()
    apointmentform = ApointmentForm
    if request.method == 'POST':
        apointmentform = ApointmentForm(request.POST)
        if apointmentform.is_valid():
            apointmentform.save()
            apointment_name = apointmentform.cleaned_data['name']
            messages.success(request, f'Gracias {apointment_name}, Se ha enviado tu cita exitosamente. Nos pondremos en contacto contigo via email')
            redirect ('index')
        else:
            messages.error(request, 'Ocurrio un error. Revise detenidamente las credenciales')
            apointmentform = ApointmentForm(request.POST)
    



    paginator = Paginator(posts, 3)  #Instanciamos con dos parametros, la variable a contar, y cuantas de estas se muestran por pagina
    page = request.GET.get('page')  #pagina actual
    posts = paginator.get_page(page)  #redefinimos post para mandar la cantidad de post segun se indico

    context={
        'posts': posts,
        'doctores': doctores,
        'apointmentform': apointmentform
    }
    return render (request, 'index.html', context=context)


def about(request):
    doctores = Doctores.objects.all()
    return render (request, 'about.html', {'doctores':doctores})


def pricing(request):
    return render (request, 'pricing.html')


def blog(request):
   

    posts = Post.objects.all().order_by('fecha_publicacion')
    posts2 = Post.objects.all().order_by('-fecha_publicacion')[:3]
    categorias = Categoria.objects.all()

    paginator = Paginator(posts, 3)  #Instanciamos con dos parametros, la variable a contar, y cuantas de estas se muestran por pagina
    page = request.GET.get('page')  #pagina actual
    posts = paginator.get_page(page)  #redefinimos post para mandar la cantidad de post segun se indico

    hoy = datetime.now().day
    queryset = request.GET.get('search')
    categoriaID = request.GET.get('categoria')

    if categoriaID:

        posts = Post.objects.filter(categoria = categoriaID)

        context={
        'posts': posts,
        'hoy':hoy,
        'categorias': categorias
        }
        return render (request, 'blog.html', context=context)
    else:
        pass


    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(previa__icontains = queryset) |
            Q(contenido__icontains = queryset),
        ).distinct()

        if posts:
            msj = f'Mostranto resultados de {queryset}'
        else:
            msj = 'No hay resultados'

        paginator = Paginator(posts, 6)
        page = request.GET.get('page') 
        posts = paginator.get_page(page)  

        context={
        'posts': posts,
        'posts2': posts2,
        'hoy':hoy,
        'msj': msj,
        'categorias': categorias
         }

        #posts = Post.objects.get(titulo__iexact = queryset).order_by('fecha_publicacion')
        return render (request, 'blog.html', context=context)


    else:
           context={
        'posts': posts,
        'posts2': posts2,
        'hoy':hoy,
        'categorias': categorias
        
         }
        

    return render (request, 'blog.html', context=context)


def service(request):
    return render (request, 'service.html')



# =========================================
#            BLOG_DETAILS
# =========================================  



def blog_details(request, id):

    posts = Post.objects.get(id=id)
    post_c = get_object_or_404(Post, id=id)
    post = Post.objects.all().order_by('-fecha_publicacion')
    posts2 = Post.objects.all().order_by('-fecha_publicacion')[:3]
    comment = post_c.comments.filter(status = True)
    categorias = Categoria.objects.all()
    comment_form = CommentForm()

    paginator = Paginator(post, 3)  #Instanciamos con dos parametros, la variable a contar, y cuantas de estas se muestran por pagina
    page = request.GET.get('page')  #pagina actual
    post = paginator.get_page(page)  #redefinimos post para mandar la cantidad de post segun se indico

    categoriaID = request.GET.get('categoria')
    hoy = datetime.now().day
    queryset = request.GET.get('search')

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post_c
            new_comment.save()
   
            messages.success(request, 'Se agrego su comentario correctamente')
            return redirect('blog_details', posts.id)
        else:
             messages.success(request, 'Hubo un error al postear su comentario. Reintentalo')
             return redirect('blog_details', posts.id)
        

           



    if categoriaID:

        posts = Post.objects.filter(categoria = categoriaID)

        context={
        'posts': posts,
        'hoy':hoy,
        'categorias': categorias
        }
        return render (request, 'blog.html', context=context)
    else:
        pass
    
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(previa__icontains = queryset) |
            Q(contenido__icontains = queryset),
        ).distinct()

        if posts:
            msj = f'Mostranto resultados de {queryset}'
        else:
            msj = 'No hay resultados'

        paginator = Paginator(posts, 6)
        page = request.GET.get('page') 
        posts = paginator.get_page(page)  

        context={
        'posts': posts,
        'posts2': posts2,
        'hoy':hoy,
        'msj': msj,
        'categorias': categorias
         }

        #posts = Post.objects.get(titulo__iexact = queryset).order_by('fecha_publicacion')
        return render (request, 'blog.html', context=context)


    else:
           context={
        'posts': posts,
        'posts2': posts2,
        'hoy':hoy,
        'categorias': categorias
         }

    context={
        'post':post,
        'categorias': categorias,
        'posts':posts,
        'comments': comment,
        'comments_form': comment_form
    
    }

    return render (request, 'blog-details.html', context=context)

# =========================================
#             END BLOG_DETAILS 
# =========================================  

def contact(request):
    form = MessageForm()
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            #se puede enviar un email con estos datos
            messages.success(request, f'Gracias {name}!  Se envio su mensaje correctamente')
            redirect ('sent')
        else:
            messages.error(request, 'ocurrio un error en el formulario. Por favor revise sus credenciales e intentalo de nuevo')
            redirect ('contact')
    return render (request, 'contact.html', {'form':form})


def sent(request):
    if messages:
        messages.success(request, f'Gracias !  Se envio su mensaje correctamente')
        redirect ('contact')
    
    return render (request, 'message_confirm.html')



# =========================================
#             TIENDA SECTION 
# =========================================            


def tienda(request):
    return render (request, 'tienda.html')