global figure
def figure(src="", caption=""):
    return f"""<figure>
        <img src="{ src }" alt="{ caption }" style="width:100%" loading="lazy">
        <figcaption>{ caption }</figcaption>
    </figure>"""

global gist
def gist(src="", file=""):
    if file == "":
        return f"""<script src="https://gist.github.com/{ src }.js"></script>"""
    else:
        return f"""<script src="https://gist.github.com/{ src }.js?file={ file }"></script>"""

global publication_card
def publication_card(title="", conference="", authors="", paper_link="", code_link="", website_link="", small_text="", abstract=""):
    links = []
    if paper_link:
        links.append(f'<a class="pub-card-link" href="{paper_link}">Paper</a>')
    if code_link:
        links.append(f'<a class="pub-card-link" href="{code_link}">Code</a>')
    if website_link:
        links.append(f'<a class="pub-card-link" href="{website_link}">Website</a>')
    links_html = f'<div class="pub-card-links">{" ".join(links)}</div>' if links else ""
    if abstract:
        toggle_html = '<div class="pub-card-abstract-actions"><button type="button" class="pub-card-abstract-toggle" aria-expanded="false">Abstract <span class="pub-card-caret">&#9662;</span></button></div>'
        abstract_html = f'<div class="pub-card-abstract"><div class="pub-card-abstract-inner"><p>{abstract}</p></div></div>'
    else:
        toggle_html = ""
        abstract_html = ""
    venue_html = f'<div class="pub-card-venue">{conference}</div>' if conference else ""
    authors_html = f'<p class="pub-card-authors">{authors}</p>' if authors else ""
    if small_text:
        small_text_html = f'<small class="pub-card-small-text">{small_text}</small>'
    else:
        small_text_html = ""
    return f"""<article class="pub-card">
        <h3 class="pub-card-title">{title}</h3>
        {authors_html}
        {small_text_html}
        {venue_html}
        {links_html}
        {toggle_html}
        {abstract_html}
    </article>"""

global author_card
def author_card(name="", tagline="", photo="", links=None):
    links = links or []
    photo_html = f'<img class="author-card-photo" src="{photo}" alt="{name}" loading="eager">' if photo else '<div class="author-card-photo"></div>'
    link_items = " · ".join(
        f'<a href="{href}">{label}</a>' for (label, href) in links
    )
    return f"""<section class="author-card">
        {photo_html}
        <div class="author-card-body">
            <h1 class="author-card-name">{name}</h1>
            <p class="author-card-tagline">{tagline}</p>
            <div class="author-card-links">{link_items}</div>
        </div>
    </section>"""
