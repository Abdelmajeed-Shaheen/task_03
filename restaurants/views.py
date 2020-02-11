from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
            "my_list":[
                    {
                            "restaurant_name":"WINGERS",
                            "food_type":"Burgers & Wings",
                            "opens_at":"12PM",
                            "closes_at":"12AM",
                    },
                    {
                            "restaurant_name":"MAC",
                            "food_type":"Fast Food",
                            "opens_at":"4am",
                            "closes_at":"--",
                    },
                    {
                            "restaurant_name":"BK",
                            "food_type":"Burgers",
                            "opens_at":"12PM",
                            "closes_at":"03AM",
                    },
                    {
                            "restaurant_name":"KFC",
                            "food_type":"Burgers & Wings",
                            "opens_at":"01PM",
                            "closes_at":"12AM",
                    },

            ]
    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
        "my_object": {
                "title":"WINGERS",
                "restaurant_name":"WINGERS",
                "food_type":"Burgers & Wings",
                "opens_at":"12PM",
                "closes_at":"12AM",
        },

    }
    return render(request, 'detail.html', context)
