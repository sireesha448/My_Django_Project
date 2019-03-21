from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import View,UpdateView
from .models import Admin,ApprovalUsers,AcceptedUsers,RejectedUser,Thoughts,Events,Technical,WorkExperience,Property,ShareMarket,Reference,Matrimonial,Celebrations,Travel
from django.views.generic import FormView
from .forms import UserRegisterForm,UserEventsForm,UserThoughtsForm,UserTechnicalForm,UserWorkExperienceForm,UserPropertyForm,UserShareMarketForm,UserReferenceForm,UserCelebrationsForm,UserMatrimonialForm,UserTravelForm


class RegisterNewUser(FormView):
    form_class = UserRegisterForm
    Model = ApprovalUsers
    template_name = "Userview/register.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        address = form.cleaned_data['address']
        email_id = form.cleaned_data['email_id']
        contact_no = form.cleaned_data['contact_no']
        date_of_birth = form.cleaned_data['date_of_birth']
        company_name = form.cleaned_data['company_name']
        status = "pending"
        ApprovalUsers(username=username,password=password,address=address,email_id=email_id,date_of_birth=date_of_birth,contact_no=contact_no,company_name=company_name,status=status).save()
        return super().form_valid(self)

class LoginCheck(View):
    def post(self,request):
        username=request.POST.get("name")
        password=request.POST.get("password")
        type=request.POST.get("type")
        if type=="admin":
            qs=Admin.objects.filter(username=username,password=password)
            if qs:
                return render(request,"Adminview/admin_menu.html")
            else:
                return render(request,"login.html",{"msg":"Invlid Details"})
        elif type=="user":
            qs=AcceptedUsers.objects.filter(username=username,password=password)
            if qs:
                return render(request,"Userview/usermenu.html")
            else:
                return render(request,"login.html",{"msg":"Invalid User Details"})
        else:
            return render(request,"login.html",{"msg":"Invalid Details"})

class Accept(View):
        def post(self,request):
            employee_id=request.POST.get("idno")
            username = request.POST.get("name")
            password = request.POST.get("password")
            address = request.POST.get("address")
            email_id = request.POST.get("email")
            contact_no = request.POST.get("contact")
            company_name = request.POST.get("compname")
            status="Accepted"
            AcceptedUsers(employee_id=employee_id,username=username,password=password,address=address,email_id=email_id,contact_no=contact_no,company_name=company_name,status=status).save()
            ApprovalUsers.objects.filter(employee_id=employee_id).delete()
            res=ApprovalUsers.objects.all()
            return render(request, "Adminview/admin_menu.html", {"msg": "User accepted", "data":res})


class Reject(View):
    def post(self, request):
        employee_id = request.POST.get("idno")
        username = request.POST.get("name")
        password = request.POST.get("password")
        address = request.POST.get("address")
        email_id = request.POST.get("email")
        contact_no= request.POST.get("contact")
        company_name = request.POST.get("compname")
        status = "Rejected"
        RejectedUser(employee_id=employee_id,username=username,password=password,address=address,email_id=email_id,contact_no=contact_no,company_name=company_name,status=status).save()
        ApprovalUsers.objects.filter(employee_id=employee_id).delete()
        res = ApprovalUsers.objects.all()
        return render(request, "Adminview/admin_menu.html", {"msg": "User Rejected", "data": res})


class AddThoughts(FormView):
    form_class = UserThoughtsForm
    model = Thoughts
    template_name = "Userview/addthought.html"
    success_url = "/usermenu/"

    def form_valid(self, form):
        username=form.cleaned_data['username']
        description=form.cleaned_data['Description']
        contact_no=form.cleaned_data['Contact_No']
        Thoughts(username=username,description=description,contact_no=contact_no).save()
        return super().form_valid(self)


class AddEvents(FormView):
    form_class = UserEventsForm
    model = Events
    template_name = "Userview/addevent.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username=form.cleaned_data['username']
        startdate=form.cleaned_data['startdate']
        enddate=form.cleaned_data['enddate']
        description=form.cleaned_data['description']
        contact_no=form.cleaned_data['contact_No']
        Events(username=username,startdate=startdate,enddate=enddate,description=description,contact_no=contact_no).save()
        return super().form_valid(self)


class AddTechnical(FormView):
    form_class = UserTechnicalForm
    model = Technical
    template_name = "Userview/addtechnical.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username=form.cleaned_data['username']
        technology=form.cleaned_data['technology']
        print(technology)
        description=form.cleaned_data['description']
        contact_no=form.cleaned_data['contact_no']
        Technical(username=username,technology=technology,description=description,contact_no=contact_no).save()
        return super().form_valid(self)

class AddWorkExperience(FormView):
    form_class = UserWorkExperienceForm
    model = WorkExperience
    template_name = 'Userview/addworkexperience.html'
    success_url = '/usermenu/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        technology = form.cleaned_data['technology']
        workExperience = form.cleaned_data['workExperience']
        description = form.cleaned_data['description']
        contact_no = form.cleaned_data['contact_no']
        WorkExperience(username=username,technology=technology,workExperience=workExperience,description=description,contact_no=contact_no).save()
        return super().form_valid(self)


class AddProperty(FormView):
    form_class = UserPropertyForm
    model = Property
    template_name = "Userview/addproperty.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        property_type = form.cleaned_data['property_type']
        property_title = form.cleaned_data['property_title']
        area_in_size = form.cleaned_data['area_in_size']
        price = form.cleaned_data['price']
        address = form.cleaned_data['address']
        contact_no = form.cleaned_data['contact_no']
        email_id = form.cleaned_data['email_id']
        Property(username=username,property_type=property_type,property_title=property_title,area_in_size=area_in_size,price=price,address=address,contact_no=contact_no,email_id=email_id).save()
        return super().form_valid(self)


class AddShareMarket(FormView):
    form_class = UserShareMarketForm
    model = ShareMarket
    template_name = "Userview/addsharemarket.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        company_name = form.cleaned_data['company_name']
        share_value = form.cleaned_data['share_value']
        description = form.cleaned_data['description']
        ShareMarket(username=username,company_name=company_name,share_value=share_value,description=description).save()
        return super().form_valid(self)

class AddReference(FormView):
    form_class = UserReferenceForm
    model = Reference
    template_name = "Userview/addreference.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        job_title = form.cleaned_data['job_title']
        description = form.cleaned_data['description']
        last_date = form.cleaned_data['last_date']
        Reference(username=username,job_title=job_title,description=description,last_date=last_date).save()
        return super().form_valid(self)


class AddMatrimonial(FormView):
    form_class = UserMatrimonialForm
    model = Matrimonial
    template_name = "Userview/addmatrimonial.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        bride_or_bridegromname = form.cleaned_data['bride_or_bridegromname']
        gender = form.cleaned_data['gender']
        date_of_birth = form.cleaned_data['date_of_birth']
        description = form.cleaned_data['description']
        contact_no = form.cleaned_data['contact_no']
        Matrimonial(bride_or_bridegromname=bride_or_bridegromname,gender=gender,date_of_birth=date_of_birth,description=description,contact_no=contact_no).save()
        return super().form_valid(self)


class AddCelebrations(FormView):
    form_class = UserCelebrationsForm
    model = Celebrations
    template_name = "Userview/addcelebrations.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        name = form.cleaned_data['name']
        address = form.cleaned_data['address']
        contact_no = form.cleaned_data['contact_no']
        email_id = form.cleaned_data['email_id']
        date_of_birth = form.cleaned_data['date_of_birth']
        Celebrations(name=name,address=address,contact_no=contact_no,email_id=email_id,date_of_birth=date_of_birth).save()
        return super().form_valid(self)



class AddTravel(FormView):
    form_class = UserTravelForm
    model = Travel
    template_name = "Userview/addtravel.html"
    success_url = '/usermenu/'

    def form_valid(self, form):
        username = form.cleaned_data['username']
        travel_date = form.cleaned_data['travel_date']
        location = form.cleaned_data['location']
        description = form.cleaned_data['description']
        contact_no = form.cleaned_data['contact_no']
        Travel(username=username,travel_date=travel_date,location=location,description=description,contact_no=contact_no).save()
        return super().form_valid(self)


