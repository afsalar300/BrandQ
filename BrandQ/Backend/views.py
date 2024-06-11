from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import categorydb, productdb, category2
from Frontend.models import orderdb


# Create your views here.
def index(request):
    return render(request, 'homepage.html')


def Addcategory(request):
    return render(request, 'Addcategory.html')
def categorydata(request):
    if request.method == 'POST':
        a = request.POST.get('category_name')
        b = request.POST.get('category_description')
        c = request.FILES['category_image']
        obj = categorydb(ca_name=a, ca_description=b, ca_image=c)
        obj.save()
        return redirect(Addcategory)
def caytegorytable(request):
    category = categorydb.objects.all()
    return render(request,'categorytable.html',{'category': category})
# page for editing
def cateEdit(request,data1):
    ca = categorydb.objects.get(id=data1)
    return render(request, 'categoryedit.html', {'ca': ca})
# for editing table
def cateEditupdate(request, data2):
    if request.method == 'POST':
        j = request.POST.get('category_name')
        k = request.POST.get('category_description')
        try:
            l = request.FILES['category_image']
            fs = FileSystemStorage()
            file = fs.save(l.name,l)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=data2).ca_image
        categorydb.objects.filter(id=data2).update(ca_name=j,ca_description=k,ca_image=file)
        return redirect(caytegorytable)
def deletecat(request, cadata):
    data = categorydb.objects.filter(id=cadata)
    data.delete()
    return redirect(caytegorytable)


def Addcategory2(request):
    return render(request,'Addcategory2.html')

def categorydata2(request):
    if request.method == 'POST':
        aa = request.POST.get('category2_name')
        ab = request.POST.get('category2_description')
        ad = request.FILES['category2_image']
        obj = category2(ca2_name=aa, ca2_description=ab, ca2_image=ad)
        obj.save()
        return redirect(Addcategory2)

def categorytable2(request):
    ca2 = category2.objects.all()
    return render(request, 'categorytable2.html', {'ca2': ca2})

def cateEdit2(request,data3):
    cat2 = category2.objects.get(id=data3)
    return render(request,'categoryedit2.html', {'cat2': cat2})

def cateEditupdate2(request, data2):
    if request.method == 'POST':
        ae = request.POST.get('category2_name')
        af = request.POST.get('category2_description')
        try:
            c = request.FILES['category2_image']
            fss = FileSystemStorage()
            file = fss.save(c.name,c)
        except MultiValueDictKeyError:
            file = category2.objects.get(id=data2).ca2_image
        category2.objects.filter(id=data2).update(ca2_name=ae,ca2_description=af,ca2_image=file)
        return redirect(categorytable2)

def deletecategory2(request,categ2):
    data = category2.objects.filter(id=categ2)
    data.delete()
    return redirect(categorytable2)


def Addproduct(request):
    catname = categorydb.objects.all()
    return render(request, 'Addproduct.html',{'catname': catname})
def productdata(request):
    if request.method == "POST":
        d = request.POST.get('ca_name')
        e = request.POST.get('product_name')
        f = request.POST.get('product_description')
        g = request.POST.get('price')
        h = request.POST.get('stock')
        i = request.FILES['product_image']
        j = request.FILES['product_imagee']
        k = request.FILES['product_imageee']
        obj = productdb(cat_name=d, pro_name=e, pro_description=f, pro_price=g, pro_stock=h, pro_product_image=i, pro_product_imagee=j, pro_product_imageee=k)
        obj.save()
        return redirect(Addproduct)

def producttable(request):
    product = productdb.objects.all()
    return render(request, 'producttable.html',{'product': product})
def productedit(request,data3):
    pro = productdb.objects.get(id=data3)
    return render(request, 'productedit.html', {'pro': pro})
def productupdate(request, data4):
    if request.method == 'POST':
        m = request.POST.get('productca_name')
        n = request.POST.get('product_name')
        o = request.POST.get('product_description')
        p = request.POST.get('price')
        q = request.POST.get('stock')
        try:
            s = request.FILES['product_image']
            fs = FileSystemStorage()
            file1 = fs.save(s.name,s)
        except MultiValueDictKeyError:
            file1 = productdb.objects.get(id=data4).pro_product_image
        try:
            s2 = request.FILES['product_imagee']
            fs = FileSystemStorage()
            file2 = fs.save(s2.name,s2)
        except MultiValueDictKeyError:
            file2 = productdb.objects.get(id=data4).pro_product_imagee
        try:
            s3 = request.FILES['product_imageee']
            fs = FileSystemStorage()
            file3 = fs.save(s3.name,s3)
        except MultiValueDictKeyError:
            file3 = productdb.objects.get(id=data4).pro_product_imageee
        productdb.objects.filter(id=data4).update(cat_name=m,pro_name=n,pro_description=o,pro_price=p,pro_stock=q,pro_product_image=file1,pro_product_imagee=file2,pro_product_imageee=file3)
        return redirect(producttable)
def prodelete(request,prodata):
        prdata = productdb.objects.filter(id=prodata)
        prdata.delete()
        return redirect(producttable)

def addproduct2(request):
    catname2 = category2.objects.all()
    return render(request,'addproduct2.html', {'catname2': catname2})

def productdata2(request):
    if request.method == "POST":
        p1 = request.POST.get('ca2_name')
        p2 = request.POST.get('product2_name')
        p3 = request.POST.get('product2_description')
        p4 = request.POST.get('price2')
        p5 = request.POST.get('stock2')
        p6 = request.FILES['product2_image']
        p7 = request.FILES['product2_imagee']
        p8 = request.FILES['product2_imageee']
        obj = productdb(cat_name=p1, pro_name=p2, pro_description=p3, pro_price=p4, pro_stock=p5, pro_product_image=p6, pro_product_imagee=p7, pro_product_imageee=p8)
        obj.save()
        return redirect(addproduct2)

def Placed_order_detail(request):
    order = orderdb.objects.all()
    return render(request, 'Placed_Orders.html', {'order': order})

