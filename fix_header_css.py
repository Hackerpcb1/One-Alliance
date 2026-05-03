from pathlib import Path
import re
root = Path(r'c:\Users\Angel\OneDrive\Desktop\Pishing de One')
files = ['sobre-nosotros.html','contacto.html','lineas-personales.html','lineas-comerciales.html','informativa-480.html']
css_block = '''  <meta name="google" content="notranslate">
  <link rel="dns-prefetch" href="//www.googletagmanager.com">
  <link rel="dns-prefetch" href="//stats.wp.com">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css?family=Fira+Sans:400,700,500,300,600,800,900%7CPoppins:700,700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="https://oneallianceinsurance.com/wp-content/plugins/elementor/assets/lib/font-awesome/css/all.min.css">
  <link rel="stylesheet" href="css/01-wp-img-auto-sizes-contain-inline-css.css">
  <link rel="stylesheet" href="css/01-wp-emoji-styles-inline-css.css">
  <link rel="stylesheet" href="css/01-classic-theme-styles-inline-css.css">
  <link rel="stylesheet" href="css/01-global-styles-inline-css.css">
  <link rel="stylesheet" href="css/01-assurena-main-inline-css.css">
  <link rel="stylesheet" href="css/07-daln-inline.css">
  <link rel="stylesheet" href="css/08-elementor-lazyload.css">
  <link rel="stylesheet" href="css/01-dynamic-css.css">
  <link rel="stylesheet" href="css/home-fixes.css">
  <link rel="stylesheet" href="css/icon-fallback.css">
  <link rel="stylesheet" href="css/sobre-nosotros.css">'''
for name in files:
    path = root / name
    text = path.read_text(encoding='utf-8')
    pattern = re.compile(r'(<head>\s*<meta charset="UTF-8">\s*<meta name="viewport"[^>]*>\s*(?:<meta http-equiv="X-UA-Compatible"[^>]*>\s*)?<title>.*?</title>).*?</head>', re.S)
    m = pattern.search(text)
    if not m:
        raise SystemExit(f'Pattern not found in {name}')
    new_text = pattern.sub(lambda mo: mo.group(1) + '\n' + css_block + '\n</head>', text, 1)
    path.write_text(new_text, encoding='utf-8')
    print(f'Updated {name}')
