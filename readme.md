# IDVC - Idly Dose Vada Coffee Price Survey
I have been collecting Idly/Dose/Vade/Coffee price in Bangalore Darshini's for fun and may be for future analysis.

Project Page : [https://thejeshgn.com/projects/idly-dose-vada-coffee-price-survey/](https://thejeshgn.com/projects/idly-dose-vada-coffee-price-survey/)

# Collection
- Is collected using [Kobo Toolbox](https://ee.kobotoolbox.org/x/WxRqhnT6)
- You can submit too. It needs a free account.

# Data
- Data is licensed under Open Data Commons Open Database License (ODbL)
- The data is in JSON format
- check `data/data.json`
```
{
    "id": "15435e6e-4334-440d-92cd-734f9b2671d7",
    "key": "15435e6e-4334-440d-92cd-734f9b2671d7",
    "value":
    {
        "_id": "15435e6e-4334-440d-92cd-734f9b2671d7",
        "_rev": "3-81cb11727286832d9681f99d1f17cfb6",
        "type": "data",
        "name_of_restaurant": "",
        "idly_two": 50,
        "masala_dosa": 50,
        "vada": 25,
        "regular_coffee": 12,
        "mini_coffee": null,
        "ac": "no",
        "type_of_restaurant":
        [
            "standing_sitting_inside"
        ],
        "lat": "12.834402",
        "lng": "77.694378",
        "submission_time": "2022-05-26T01:40:45.00+05:30",
        "submitted_by": ""
    }
}
```



# Code
- Currently code is just to reformat the data got from Kobocollect and load to CouchDB