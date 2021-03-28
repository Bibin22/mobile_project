{% extends 'app_mobile/base.html' %}
{% block body_block %}

 <section id="listing" class="py-4">
    <div class="container">

      <div class="row">
        <div class="col-md-9">
          <!-- Home Main Image -->
          <img src="{{ mobiles.image }}">
          <!-- Thumbnails -->
          <div class="row mb-5 thumbs">
            {% if mobiles.image_1 %}
            <div class="col-md-2">

              <a href="{{ mobiles.image_1 }}" data-lightbox="home-images">
                <img src="{{ mobiles.image_1 }}" alt="" class="img-fluid">
              </a>
            </div>
            {% endif %}
            {% if mobiles.image_2 %}
            <div class="col-md-2">
              <a href="{{ mobiles.image_2 }}" data-lightbox="home-images">
                <img src="{{ mobiles.image_2 }}" alt="" class="img-fluid">
              </a>
            </div>
            {% endif %}
            {% if mobiles.image_3 %}
            <div class="col-md-2">
              <a href="{{ mobiles.image_3 }}" data-lightbox="home-images">
                <img src="{{ mobiles.image_3 }}" alt="" class="img-fluid">
              </a>
            </div>
              {% endif %}




          <!-- Description -->
          <div class="row mb-5">
            <div class="col-md-12">
             {{ mobiles.brand_name }}
                {{ mobiles.model_name }}
                {{ mobiles.specifications }}
            </div>
          </div>
        </div>

      </div>
    </div>
  </section>
           <a href="{% url 'order' mobiles.id %}" class="btn btn-outline-primary">Place Order</a>



{% endblock %}