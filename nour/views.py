from django.shortcuts import get_object_or_404, render
from .models import Servies , Team , Product , Price_left , Price_right , Gallery , Nails , Eye , Lips ,Eyebrows , Dress
# Create your views here.
def services_list(request  ):
    services = Servies.objects.all()
    team = Team.objects.all()
    product = Product.objects.all()
    price1 = Price_left.objects.all()
    price2 = Price_right.objects.all()
    gallery = Gallery.objects.all()
    return render(request ,'nour/index.html',{'services' : services , 'team' : team , 'product' :product , 'price_left' : price1 , 'price_right' : price2, 'gallery' : gallery})


def service_detail(request, id):
    # جلب الخدمة المحددة بناءً على id
    service = Servies.objects.get( id=id)

    # تحديد نوع الخدمة لجلب العناصر المرتبطة بها
    if service.name == "أظافر":  # افتراض أن اسم الخدمة يحدد نوعها
        items = Nails.objects.all()
    elif service.name == "اكستنشن رموش":
        items = Eye.objects.all()
    elif service.name == "توريد شفايف":
        items = Lips.objects.all()
    elif service.name == "تاتو  حواجب":
        items = Eyebrows.objects.all()
    elif service.name == "تأجير فساتين":
        items = Dress.objects.all()
    else:
        items = []  # في حال كانت الخدمة غير معروفة

    return render(request, 'nour/service_detail.html', {
        'service': service,
        'items': items,
    })

