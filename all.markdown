---
layout: default
title:  "All"
date:   2017-08-30
categories: gallery
---

# All Works

This gallery presents the complete collection of works mapped to-date in collection-order.


## Gallery

<ul class="photo-gallery">
{% for image in site.static_files %}
  {% if image.name contains '.png' and image.path contains 'gamebooks/thumb' %}
    {% assign image_book_id = image.basename | truncate: 5, "" %}
    <figure style="display: inline-block; text-align: center;">
      <a href="{{ site.baseurl }}/gamebooks/{{ image_book_id }}.html#{{ image.basename }}" target="_blank"><img src="{{ site.baseurl }}/assets/gamebooks/thumb/{{ image.name }}" alt="image"/></a>
      <figcaption>{{ image_book_id }}</figcaption>
    </figure>
  {% endif %}
{% endfor %}
</ul>
