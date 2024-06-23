from django.shortcuts import render, redirect
from django.contrib import messages
import requests

# GET request
def get_api_data(request):
    url = 'http://localhost:8085/finapi/category/'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return render(request, 'api_data.html', {'apidata': data})
        else:
            messages.warning(request, "Failed to retrieve data from the API.")
    except Exception as ex:
        print(ex)
        messages.warning(request, "An error occurred while fetching data.")
    return render(request, 'index.html')

# POST request
def do_post_data(request):
    url = 'http://localhost:8085/finapi/category/'
    if request.method == "POST":
        cname = request.POST.get('txtName')
        bplan = request.POST.get('budPlan')

        payload = {
            'cat_name': cname, 
            'budget': bplan
            }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 201:
                data = response.json()
                messages.success(request, f"Details stored successfully with ID: {data['cat_id']} and Name: {data['cat_name']}")
            else:
                messages.warning(request, "Failed to save data.")
        except Exception as ex:
            print(ex)
            messages.warning(request, "An error occurred during the save process.")
    return render(request, 'category_add.html')



# --------------- PUT = update all----------------------
def do_put_data(request, cat_id):
    url = 'http://127.0.0.1:8085/finapi/category/' + str(cat_id) + '/'  # must teminate with /

    if request.method == "POST":
        
        # get data from form
        cname = request.POST.get('txtName')
        bplan = request.POST.get('budPlan')
        
        # cstatus = request.POST.get('rating') checkbox handling later
       

        payload = {
            'cat_name': cname,
            'budget': bplan
            
        }

        response = requests.put(url, json = payload)  # send as JSON

        if response.status_code == 200:   # response 200
            data = response.json()   # returns a dictionary object with all the details of newly added object including Primary Key & auto updated values
            print(data)
            # return data
            messages.success(request, "Details updated successfully with Name: " + str(data["cat_name"]) + ", Budget: " + str(data["budget"]))
            
        else:
            messages.warning(request, "Some error occured during update, check logs for details")
            #return None

        return redirect('/getdata')  # redirect to view all

    else:  # * * * * * * * get details of the selected company by API Call  * * * * * * * 

        response = requests.get(url) #.json()
        if response.status_code == 200:
            data = response.json()
            return render(request, 'category_edit.html', {'apidata' : data})
        

# --------------- PATCH (limited fields)----------------------
def do_patch_data(request, cat_id):
    url = 'http://127.0.0.1:8085/finapi/category/' + str(cat_id) + '/'  # must teminate with /

    cname = request.POST.get('txtName')

    payload = {
        'cat_name': cname
    }
    response = requests.patch(url, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


# --------------- DELETE (One)----------------------
def do_delete_data(request, cat_id):
    url = 'http://127.0.0.1:8085/finapi/category/' + str(cat_id) + '/'

    try:
        response = requests.delete(url)
    
        if response.status_code == 204:
            messages.success(request, "Details deleted successfully")
        else:
            messages.warning(request, "Failed to delete resource..remote server did not respond properly")
    except Exception as ex:
        print(ex)
        messages.warning(request, "Some error occured during delete, check logs for details")

    return redirect('/getdata')



#-============ using URLLIB ======================
def home(request):
    try:
        response = rq.urlopen('http://127.0.0.1:8085/api/v1/category/')
        if response.code ==200:
            # return HttpResponse("Status: OK")
            print("Status: OK")
            print("Returned : ", response)
            data = response.read()
            print(type(data))
            print('Length : ', len(data))
            print('Meta data ', response.peek())
            # content = data.decode("json")
            # print(content)
    except Exception as ex:
        messages.warning(request, "Some error occured")
    return render(request, 'index.html')



def getactdata(request):
    url = 'http://localhost:8085/finapi/activity/'
    
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            print(data)
            return render(request, 'activity.html', {'acdata': data})
        else:
            messages.warning(request, "Failed to retrieve data from the API.")
    except Exception as ex:
        print(ex)
        messages.warning(request, "An error occurred while fetching data.")
    return render(request, 'index.html')

# POST request
def saveactdata(request):
    url = 'http://localhost:8085/finapi/activity/'
    if request.method == "POST":
        aname = request.POST.get('txtActName')
        adesc = request.POST.get('acdesc')
        exp = request.POST.get('expense')
        adate = request.POST.get('acdate')

        payload = {
            'ac_name': aname, 
            'ac_desc':adesc,
            
            'expense': exp,
            'a_date':adate,
            }

        try:
            response = requests.post(url, json=payload)
            if response.status_code == 201:
                data = response.json()
                messages.success(request, f"Details stored successfully with ID: {data['ac_id']} and Name: {data['ac_name']}")
            else:
                messages.warning(request, "Failed to save data.")
        except Exception as ex:
            print(ex)
            messages.warning(request, "An error occurred during the save process.")
    return render(request, 'act_add.html')

