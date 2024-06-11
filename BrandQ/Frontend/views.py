from django.contrib import messages
from django.core.mail import EmailMessage

from django.shortcuts import render, redirect

from Backend.models import categorydb, category2, productdb, cart_data, contactDB
from Frontend.models import loginsavedb, orderdb


# Create your views here.
def loginpage(request):
    return render(request, 'loginpage.html')


def logindetail(request):
    if request.method == 'POST':
        b = request.POST.get('name')
        a = request.POST.get('mail')
        c = request.POST.get('pass')
        if loginsavedb.objects.filter(user_email=a).exists():
            messages.error(request, 'Email already exists.')
            return redirect('loginpage')
        obj = loginsavedb(user_name=b, user_email=a, user_password=c)
        obj.save()
        messages.success(request, 'Sign up successful!')
        return redirect(loginpage)


def login(request):
    if request.method == 'POST':
        d = request.POST.get('email')
        e = request.POST.get('pas')
        if loginsavedb.objects.filter(user_email=d, user_password=e).exists():
            request.session['user_email'] = d
            request.session['user_password'] = e
            messages.success(request, 'Login successful.')
            return redirect(homepage)
        else:
            messages.error(request, 'User not found.')
            return redirect(loginpage)


def logout(request):
    del request.session['user_email']
    del request.session['user_password']
    return redirect(loginpage)


def homepage(request):
    category = category2.objects.all()
    cate = categorydb.objects.all()
    return render(request, 'homepage.html', {'category': category, 'cate': cate})


def search_result(request):
    query = request.GET.get('q')
    search_categories = request.GET.get('search_categories')

    if query:
        # Query products
        product_results = productdb.objects.filter(pro_name=query)
        # Query categories if requested
        category_results = productdb.objects.filter(cat_name=query) if search_categories else []
        # Combine results
        result = list(product_results) + list(category_results)
    else:
        result = []
    return render(request, 'search.html', {'result': result})


def search_re(request, dat):
    s_data = productdb.objects.get(id=dat)
    return render(request, 'searchRe.html', {'s_data': s_data})


def search_product_to_cart(request):
    if request.method == 'POST':
        sa = request.POST.get('usermail3')
        sb = request.POST.get('pr_name3')
        sc = request.POST.get('pr_image3')
        sd = request.POST.get('qty3')
        se= request.POST.get('totalprice3')
        sf = request.POST.get('shop-sizes3')
        sg = request.POST.get('pri3')
        obj = cart_data(Useremail=sa, p_name=sb, p_image=sc, p_quantity=sd, price_total=se, p_size=sf, p_price=sg)
        obj.save()
        return redirect(cartpage)

def productpage(request, cat1):
    data = productdb.objects.filter(cat_name=cat1)
    return render(request, 'productpage.html', {'data': data})


def productpage2(request, cat2):
    data2 = productdb.objects.filter(cat_name=cat2)
    return render(request, 'productpage2.html', {'data2': data2})


def singleproduct(request, data):
    data = productdb.objects.get(id=data)
    return render(request, 'singleproduct.html', {'data': data})


def singleproduct2(request, data1):
    data2 = productdb.objects.get(id=data1)
    return render(request, 'singleproduct2.html', {'data2': data2})


def cart_datas(request):
    if request.method == 'POST':
        gg = request.POST.get('usermail2')
        g = request.POST.get('pr_name')
        h = request.POST.get('pr_image')
        i = request.POST.get('qty')
        j = request.POST.get('totalprice')
        k = request.POST.get('shop-sizes')
        l = request.POST.get('pri')
        obj = cart_data(p_name=g, p_image=h, p_quantity=i, price_total=j, p_size=k, p_price=l, Useremail=gg)
        obj.save()
        return redirect(cartpage)


def cartpage(request):
    dat = cart_data.objects.filter(Useremail=request.session['user_email'])
    total_price = sum(i.price_total for i in dat)
    return render(request, 'cart.html', {'dat': dat, 'total_price': total_price})


def cart2(request):
    if request.method == 'POST':
        mm = request.POST.get('usermail1')
        m = request.POST.get('p_name2')
        n = request.POST.get('img2')
        o = request.POST.get('qty2')
        p = request.POST.get('totalprice2')
        q = request.POST.get('shop-sizes2')
        r = request.POST.get('p_price2')
        obj = cart_data(p_name=m, p_image=n, p_quantity=o, price_total=p, p_size=q, p_price=r, Useremail=mm)
        obj.save()
        return redirect(cartpage)


def delete_cart_data(request, cartdata):
    del_data = cart_data.objects.filter(id=cartdata)
    del_data.delete()
    return redirect(cartpage)


def checkoutpage(request):
    check_data = cart_data.objects.filter(Useremail=request.session['user_email'])
    total = sum(i.price_total for i in check_data)
    return render(request, 'checkout.html', {'check_data': check_data, 'total': total})


def order_address(request):
    if request.method == 'POST':
        s = request.POST.get('country')
        t = request.POST.get('c_fname')
        u = request.POST.get('c_lname')
        v = request.POST.get('c_address')
        w = request.POST.get('apartment')
        x = request.POST.get('c_state')
        y = request.POST.get('c_postal_zip')
        z = request.POST.get('c_email_address')
        aa = request.POST.get('c_phone')
        ab_list = request.POST.getlist('product')
        ac_list = request.POST.getlist('qty')
        ad_list = request.POST.getlist('price')
        obj = orderdb(Country=s, First_Name=t, Last_Name=u, Address=v, Apartment=w, State=x, Postal_Zip=y, Email_Address=z, Phone=aa, Product=ab_list, Quantity=ac_list, Price=ad_list)
        obj.save()
        return redirect(thankyou)


def thankyou(request):
    return render(request, 'thankyou.html')


def contact(request):
    return render(request, 'contactpage.html')

def contactdata(request):
    if request.method == 'POST':
        ba = request.POST.get('c_fname')
        bc = request.POST.get('c_lname')
        bd = request.POST.get('c_email')
        be = request.POST.get('c_email')
        bf = request.POST.get('c_message')
        obj = contactDB(first_name=ba, last_name=bc, email=bd, subject=be, message=bf)
        obj.save()
        messages.success(request, 'Submitted successful!')
        return redirect(homepage)

