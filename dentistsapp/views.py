from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import MessageForm, ApointmentForm, CommentForm, CorreosForm
from django.core.paginator import Paginator
from django.contrib import messages
from datetime import datetime
from django.db.models import Q

# Create your views here.
def index(request):
    servicios = Precio.objects.all()
    posts = Post.objects.all().order_by('-fecha_publicacion')
    cursos = Curso.objects.all().order_by('-fecha_publicacion')[:3]
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
        'cursos': cursos,
        'apointmentform': apointmentform,
        'servicios': servicios
    }
    return render (request, 'index.html', context=context)


def about(request):
    doctores = Doctores.objects.all()
    return render (request, 'about.html', {'doctores':doctores})


def pricing(request):
    servicios = Precio.objects.all()

    return render (request, 'pricing.html', {'servicios': servicios})


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
#            BLOG_DETALLES
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
            new_comment.name = request.user
            new_comment.save()
   
            messages.success(request, 'Se agregó su comentario correctamente')
            return redirect('blog_details', posts.id)
        else:
             messages.success(request, 'Hubo un error al postear su comentario. Reinténtalo')
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
#             TERMINA BLOG_DETAILS 
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
            messages.success(request, f'Gracias {name}!  Se envió su mensaje correctamente')
            redirect ('sent')
        else:
            messages.error(request, 'ocurrió un error en el formulario. Por favor revise sus credenciales e inténtalo de nuevo')
            redirect ('contact')
    return render (request, 'contact.html', {'form':form})


def sent(request):
    if messages:
        messages.success(request, f'Gracias !  Se envió su mensaje correctamente')
        redirect ('contact')
    
    return render (request, 'message_confirm.html')



# =========================================
#             TIENDA SECTION 
# =========================================            


def contenido_educativo(request):
    cursos = Curso.objects.all().order_by('-fecha_publicacion')
    # busqueda = request.GET.get('q')
    # datos_totales = datos.count()

    paginas = Paginator(cursos, 6)
    page = request.GET.get('page') 
    cursos = paginas.get_page(page)
    busqueda = request.GET.get('q')


    if busqueda:
          cursos = Curso.objects.filter(
             Q(titulo__icontains = busqueda) |  Q(acerca__icontains = busqueda)  | Q(lecciones__icontains = busqueda) 
         ).distinct()
          cursos_totales = cursos.count()
          
          paginas = Paginator(cursos, 6)
          page = request.GET.get('page') 
          cursos = paginas.get_page(page)


          return render (request, 'tienda.html', {'cursos': cursos, 'cursos_totales': cursos_totales})
    else:
        pass

    context = {
        'cursos' : cursos,
    }

    return render (request, 'tienda.html', context=context)


def curso(request, titulo):
    cursos = Curso.objects.get(titulo=titulo)
    otros_cursos = Curso.objects.all().order_by('-fecha_publicacion')[:3]
    context = {
        'cursos': cursos,
        'otros': otros_cursos,
    }

    return render (request, 'curso.html', context=context)

# =========================================
#               CORREOS 
# =========================================            

def correos(request):
    form = CorreosForm()
    if request.method == 'POST':
        form = CorreosForm(request.POST)
        if form.is_valid(): 
            form.save()
            return render(request, 'correos.html')
    context={
        'form': form
    }
    return render(request, 'correos.html', context)