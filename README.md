# Short and Sweet
Comprehensive Approach for Summing up Application’s Reviews using NLP


## LIST OF ENDPOINTS:

1. **Endpoint:** `/backend/app_data/`
   - **HTTP Method:** GET
   - **Arguments:**
     - `url` (str)
     - `stars` (int, optional)
     - `count` (int, optional)
     - `inssuficien` (bool, optional)
     - `invalid_url` (bool, optional)

**Example return value**:
```json
{
  "title": "Google Maps",
  "icon": "https://play-lh.googleusercontent.com/Kf8WTct65hFJxBUDm5E-EpYsiDoLQiGGbnuyP6HBNax43YShXti9THPon1YKB6zPYpA",
  "reviews": 2239
}
```

**404 error detail**
```json
  "detail": "App did not recive sufficient number of reviews"
```
or 
```json
  "detail": "Invalid URL. Make sure URL is from english version of the site."
```
---
2. **Endpoint:** `/backend/request_inference/bertopic/`
   - **HTTP Method:** GET
   - **Arguments:** None

**Example return value**
```json
{
  "topics": {
    "0": "phone_app_service_picture",
    "1": "instagram_time_bad_habbit",
    "2": "cant_open_camera_error"
  },
  "counts": {
    "0": 990,
    "1": 201,
    "2": 40
  }
}
```
---
3. **Endpoint:** `/backend/request_inference/distilbert/`
   - **HTTP Method:** GET
   - **Arguments:** None

**Example return value**
```json
{
  "positive": 2402,
  "neutral": 10,
  "negative": 90
}
```
---
4. **Endpoint:** `/backend/more_data/`
   - **HTTP Method:** GET
   - **Arguments:**
     - `cluster` (int)
     - `results_not` (bool, optional)

**Example return value**
```json
{
  "cluster": "cant_open_camera_error",
  "reviews": [
    {
      "review": "Est quaerat sed dolorem ipsum numquam neque. Etincidunt etincidunt dolor labore. Non sed dolore ipsum dolore tempora. Modi quiquia labore aliquam dolorem porro voluptatem. Non dolorem magnam labore quaerat dolore non. Labore adipisci eius adipisci neque etincidunt aliquam.",
      "thumbs_up_count": 53,
      "sentiment": -1
    },
    {
      "review": "Tempora non consectetur adipisci quaerat ipsum. Modi eius neque tempora velit tempora. Est porro dolore sit labore quaerat non. Numquam neque est adipisci. Magnam dolorem quiquia neque velit. Sed labore adipisci dolor sed magnam. Tempora numquam ut magnam velit labore eius quiquia.",
      "thumbs_up_count": 3,
      "sentiment": 1
    },
.
.
.
  ]
}
```

**404 error detail**
```json
  "detail": "Results are not ready."
```
or
```json
 "detail": "Cluster not found."
```
