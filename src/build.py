src=open('src/site-source.html',encoding='utf-8').read()
src=src.replace('<meta name="claude:viewport-fit-sides" content="cover">\n','')
src=src.replace('<title>Football Shirt Stand</title>','<title>Football Shirt Stand | Authentic Football Shirts, Adults & Kids</title>',1)
desc="Authentic football shirts for adults and kids, checked and graded by hand. Club and national team kits shipped worldwide. Pay with PayPal, or sell us your shirts."
seo=f'''<meta name="description" content="{desc}">
<link rel="canonical" href="https://footballshirts.pt/">
<meta name="robots" content="index, follow">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Football Shirt Stand">
<meta property="og:title" content="Football Shirt Stand | Authentic Football Shirts">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://footballshirts.pt/">
<meta property="og:image" content="https://footballshirts.pt/img/benfica-front.webp">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"OnlineStore","name":"Football Shirt Stand","alternateName":"FSS","url":"https://footballshirts.pt/","email":"shop@footballshirts.pt","sameAs":["https://www.instagram.com/footballshirtstand/"],"description":"{desc}"}}</script>
'''
head='<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'+seo
j=src.find('</style>')+8
open('site/index.html','w',encoding='utf-8').write(head+src[:j]+'\n</head>\n<body>\n'+src[j:]+'\n</body>\n</html>\n')
