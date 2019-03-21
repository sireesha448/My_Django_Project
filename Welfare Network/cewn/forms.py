from django import forms

class UserRegisterForm(forms.Form):
     # employee_id = forms.IntegerField(label="Employee_Id",widget=forms.NumberInput)
     username = forms.CharField(label="Username",widget=forms.TextInput)
     password = forms.CharField(label="Password",widget=forms.PasswordInput)
     address = forms.CharField(label="Address",widget=forms.Textarea)
     email_id = forms.EmailField(label="Email_Id",widget=forms.EmailInput)
     contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digits number without country-code")
     years=range(1952,2100)
     date_of_birth = forms.DateField(label="Date Of Birth",widget=forms.SelectDateWidget(years=years))
     company_name = forms.CharField(label="Company_Name",widget=forms.TextInput)

class UserThoughtsForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    Description = forms.CharField(label="Description", widget=forms.Textarea)
    Contact_No = forms.IntegerField(label="Contact_No", widget=forms.NumberInput,help_text="enter 10 digit number only")


class UserEventsForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput)
    year = range(1990,2100)
    startdate = forms.DateField(label="Startdate", widget=forms.SelectDateWidget(years=year))
    enddate = forms.DateField(label="Enddate",widget=forms.SelectDateWidget(years=year))
    description = forms.CharField(label="Description",widget=forms.Textarea)
    contact_No = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")


class UserTechnicalForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    technology = forms.CharField(label="Technology", widget=forms.TextInput)
    description = forms.CharField(label="Description", widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")


class UserWorkExperienceForm(forms.Form):
    username = forms.CharField(label="Username", widget=forms.TextInput)
    technology = forms.CharField(label="Technology", widget=forms.TextInput)
    workExperience = forms.CharField(label='Work Experience',widget=forms.Select(choices=(('--select--','--select--'),('fresher','Fresher'),('0','0'),('1','1'),('2','2'),('3','3'),('4','4'),('5','5'),('6','6'),('7','7'),('8','8'),('9','9'),('10','10'),('10+','10+'))))
    # workexperience = forms.ChoiceField(choices=[('fresher','experience'),('fresher','fresher')])
    description = forms.CharField(label="Description",widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")


class UserPropertyForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput)
    property_type = forms.CharField(widget=forms.Select(choices=(('--select--','--select--'),('SALE', 'sale'), ('RENT', 'rent'))),label="Property Type")
    property_title = forms.CharField(label="Property Tytle",widget=forms.TextInput)
    area_in_size = forms.IntegerField(label="Area In Size",widget=forms.NumberInput,help_text="Enter in Squares[sq]")
    price = forms.DecimalField(label="Price",widget=forms.NumberInput)
    address = forms.CharField(label="Address",widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")
    email_id = forms.EmailField(label="Email_Id",widget=forms.EmailInput)


class UserShareMarketForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput)
    company_name = forms.CharField(label="Company_name",widget=forms.TextInput)
    share_value = forms.IntegerField(label="Share_value",widget=forms.NumberInput)
    description = forms.CharField(label="Description",widget=forms.Textarea)

class UserReferenceForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput)
    job_title = forms.CharField(label="Job_Title",widget=forms.TextInput)
    description = forms.CharField(label="Description",widget=forms.Textarea)
    last_date = forms.DateField(label="Last_date",widget=forms.SelectDateWidget)


class UserMatrimonialForm(forms.Form):
    bride_or_bridegromname =forms.CharField(label="Bride_or_Bridegromname",widget=forms.TextInput)
    gender = forms.CharField(label="Gender",widget=forms.Select(choices=(('MALE','male'),('FEMALE','female'))))
    date_of_birth = forms.DateField(label="Date Of Birth",widget=forms.SelectDateWidget)
    description = forms.CharField(label="Description",widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")

class UserCelebrationsForm(forms.Form):
    name = forms.CharField(label="Username",widget=forms.TextInput)
    address = forms.CharField(label='Address',widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")
    email_id = forms.EmailField(label="Email_Id",widget=forms.EmailInput)
    date_of_birth = forms.DateField(label="Date Of Birth",widget=forms.SelectDateWidget)


class UserTravelForm(forms.Form):
    username = forms.CharField(label="Username",widget=forms.TextInput)
    travel_date = forms.DateField(label="Travel Date",widget=forms.SelectDateWidget)
    location = forms.CharField(label='Location',widget=forms.Textarea)
    description = forms.CharField(label="Description",widget=forms.Textarea)
    contact_no = forms.IntegerField(label="Contact_No",widget=forms.NumberInput,help_text="enter 10 digit number only")