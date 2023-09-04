from django.shortcuts import render
from django.http import Http404
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import ListView
from .forms import EmailPostForm
from django.core.mail import send_mail


# Create your views here.
# class PostListView(ListView):
#     """
#     Alternative Post list view
#     """


def post_list(request):
    posts_list = Post.objects.filter(status=Post.Status.PUBLISHED)

    ##PAGINATION WITH 3 POSTS PER PAGE.

    #we will display 3 posts/page
    paginator = Paginator(posts_list,3) 

    #we retrive the page no. using GET method and if 
    #page parameter is not in the GET parameter of the 
    #request then we use the default value 1 to load the first page of results.
    page_number = request.GET.get("page",1)

    try:

        #we obtain the objects of the desired page by calling page() method.
        posts = paginator.page(page_number)

    # print("Previous Page num: ",posts.previous_page_number)
    # print("Current Page num: ",posts.number)
    # print("Total Page num: ",posts.paginator.num_pages)
    # print("Next Page num: ",posts.next_page_number)
    # print("Object List: ",posts.object_list)
    # print("*****************************************************************************************************************")

    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)
    
    except EmptyPage:
        # If page_number is out of range deliver last page of results
        posts = paginator.page(paginator.num_pages)
    
    posts_dict = {
            "posts":posts,
        }

    return render(request,"blog/post/list.html",context = posts_dict)


def post_detail(request,year,month,day,slug):
    try:
        post = Post.objects.get(publish__year=year, publish__month=month, publish__day=day, slug=slug, status=Post.Status.PUBLISHED)
        post_dict = {
        "post":post,
    }
    except Post.DoesNotExist:
        raise Http404("No Post found.")
    return render(request,"blog/post/detail.html",context = post_dict)



def post_share(request, post_id):

    sent = False
    #Retrive post by id
    try:
        #Retrive post by id
        post = Post.objects.get(id=post_id, status=Post.Status.PUBLISHED)
        
        
    #     post_dict = {
    #     "post":post,
    # }
        if request.method == "POST":  
            """ If the request method is POST 
            that means Form was submitted and now 
            we have to process the data from the Form"""

            form = EmailPostForm(request.POST)
            print("form:  ",form)

            if form.is_valid():
                #FORM fields passed validation
                cd = form.cleaned_data
                print("cd:  ",cd)
                #...send email
            post_url = request.build_absolute_uri(post.get_absolute_url_for_urls_post_details())

            subject = f"{cd['name']} recommends you read {post.title}"
                     
            message = f"Read {post.title} at {post_url}\n\n {cd['name']}\'s comments: {cd['comments']}" 
                      
            send_mail(subject, message, 'your_account@gmail.com',
                      [cd['to']])
            sent = True

        elif request.method == "GET":
            """ If the request method is GET 
            that means an empty form has to be displayed 
             to the user. """
            form = EmailPostForm()
        
        comfirm_dict = {'post': post, 'form': form, 'sent': sent}

    except Post.DoesNotExist:
        raise Http404("No Post found.")
    
    return render(request,'blog/post/share.html', context=comfirm_dict)
