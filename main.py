from reactpy import component, html, hooks
from reactpy.backend.fastapi import configure
from fastapi import FastAPI

@component
def Item(text, initial_done=False):
    done, set_done = hooks.use_state(initial_done)
    
    def handle_click(event):
        set_done(not done)
    
    attrs = {"style": {"color": "green"}} if done else {}
    
    if done:
        return html.li(attrs, text)
    else:
        return html.li(
            html.span(attrs, text),
            html.button({ "on_click": handle_click}, "Hecho!")
        )

@component
def HelloWorld():
    return html._(
        html.h1("Lista de tareas"),
        html.ul(
          Item("React whit python"),
          Item("Tarea 2"),
          Item("Tarea 3"),
          Item("Tarea 4", initial_done=True),
        ),
    )

app = FastAPI()
configure(app, HelloWorld)