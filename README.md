# Build instructions

This static site uses [s4g](s4g.grapheo12.in) to build the website.

Install `s4g` on your device:

```bash
pip3 install s4g --user
```

After making changes to the Markdown files in `src/`, run
```bash
s4g src public templates
```
to build the website in `public/`.
The `main` branch gets automatically deployed.