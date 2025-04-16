# Guía Rápida y Bonita: GitHub Readme Stats en Español

¿Quieres mostrar tus estadísticas y lenguajes favoritos en tu perfil de GitHub? ¡Sigue leyendo! Aquí tienes una guía sencilla, visual y en español para personalizar tus tarjetas usando tu usuario: **S4vi0r17**.

---

## ⭐ Tarjeta de Estadísticas de GitHub

Muestra tus stats principales (commits, issues, PRs, etc):

```markdown
[![Mis Stats de GitHub](https://github-readme-stats.vercel.app/api?username=S4vi0r17&show_icons=true&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

Puedes cambiar el tema por: `dark`, `merko`, `gruvbox`, `tokyonight`, `onedark`, `cobalt`, `synthwave`, `highcontrast`, `dracula`, etc.

---

## 🏆 Personaliza tu tarjeta

- Ocultar datos: `&hide=stars,commits,prs,issues,contribs`
- Mostrar más datos: `&show=reviews,discussions_started,prs_merged`
- Mostrar iconos: `&show_icons=true`
- Cambiar idioma: `&locale=es`
- Cambiar colores: `&title_color=ff69b4&text_color=ffffff&bg_color=151515`

Ejemplo avanzado:

```markdown
[![Mis Stats de GitHub](https://github-readme-stats.vercel.app/api?username=S4vi0r17&show_icons=true&hide=contribs,prs&theme=dracula&locale=es)](https://github.com/anuraghazra/github-readme-stats)
```

---

## 📊 Tarjeta de Lenguajes Más Usados

Muestra los lenguajes que más usas en tus repositorios:

```markdown
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=S4vi0r17&layout=compact&langs_count=8&theme=radical)](https://github.com/anuraghazra/github-readme-stats)
```

### Opciones útiles:
- Cambiar cantidad: `&langs_count=10`
- Ocultar lenguajes: `&hide=html,css`
- Excluir repos: `&exclude_repo=repo1,repo2`
- Cambiar diseño: `&layout=compact`, `donut`, `donut-vertical`, `pie`
- Ocultar barras: `&hide_progress=true`
- Cambiar título: `&custom_title=Lenguajes%20Favoritos`

Ejemplo avanzado:

```markdown
[![Top Langs](https://github-readme-stats.vercel.app/api/top-langs/?username=S4vi0r17&layout=donut&langs_count=6&hide=html,css&theme=gruvbox&custom_title=Lenguajes%20Favoritos)](https://github.com/anuraghazra/github-readme-stats)
```

---

## 📌 Tarjeta de Repositorio Destacado

Muestra un repo destacado en tu perfil:

```markdown
[![Repo Destacado](https://github-readme-stats.vercel.app/api/pin/?username=S4vi0r17&repo=NOMBRE_DEL_REPO)](https://github.com/S4vi0r17/NOMBRE_DEL_REPO)
```

---

## 💡 Tips Extra

- Puedes alinear varias tarjetas usando HTML:

```html
<a href="https://github.com/S4vi0r17">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api?username=S4vi0r17" />
</a>
<a href="https://github.com/S4vi0r17">
  <img height=200 align="center" src="https://github-readme-stats.vercel.app/api/top-langs?username=S4vi0r17&layout=compact&langs_count=8" />
</a>
```

- Puedes personalizar aún más con los parámetros de color y diseño.
- Si tienes problemas de límite de peticiones, considera desplegar tu propia instancia en Vercel.

---

## 📚 Recursos útiles
- [Repositorio oficial](https://github.com/anuraghazra/github-readme-stats)
- [Temas disponibles](https://github.com/anuraghazra/github-readme-stats/blob/master/themes/README.md)
- [Documentación en español](https://github.com/anuraghazra/github-readme-stats/blob/master/docs/readme_es.md)
