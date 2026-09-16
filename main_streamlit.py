import pandas as pd
import streamlit as st

st.markdown(
    "<h1 style='text-align: center;'>Gestor de Tareas</h1>",
    unsafe_allow_html=True,
)
st.write("---")

if "pendientes" not in st.session_state:
    st.session_state.pendientes = []

if "completadas" not in st.session_state:
    st.session_state.completadas = []

if "opcion_enviada" not in st.session_state:
    st.session_state.opcion_enviada = None

with st.container(border=True):
    st.subheader("Menú de Opciones")

    st.write("1. Agregar tareas")
    st.write("2. Marcar completada")
    st.write("3. Ver pendientes")
    st.write("4. Ver completadas")
    st.write("5. Salir")

    st.write("")

    menu_input = st.text_input("¿Qué desea hacer?:", key="input_menu_usuario")

    if st.button("Enviar"):
        st.session_state.opcion_enviada = menu_input.strip().lower()
        st.rerun()

opcion = st.session_state.opcion_enviada

if opcion is not None:
    st.write("---")

    if opcion in ["1", "agregar tareas", "agregar"]:
        st.subheader("➕ Agregar Nueva Tarea")

        nueva_tarea = st.text_input(
            "Añada el nombre de la tarea:", key="input_nueva_tarea"
        )

        if st.button("Guardar Tarea"):
            if nueva_tarea.strip() != "":
                st.session_state.pendientes.append(nueva_tarea)
                st.success(
                    f"La tarea: **'{nueva_tarea}'** se ha añadido correctamente."
                )
            else:
                st.warning("No ha colocado ninguna tarea.")

    elif opcion in ["2", "marcar completada", "completar"]:
        st.subheader("✅ Marcar Tarea como Completada")

        if len(st.session_state.pendientes) == 0:
            st.info("No tienes tareas pendientes por completar.")
        else:
            tarea_a_completar = st.selectbox(
                "Selecciona la tarea que terminaste:",
                options=st.session_state.pendientes,
            )

            if st.button("Marcar como completada"):
                st.session_state.pendientes.remove(tarea_a_completar)
                st.session_state.completadas.append(tarea_a_completar)
                st.success(
                    f"La tarea **'{tarea_a_completar}'** se ha marcado como completada."
                )
                st.rerun()

    elif opcion in ["3", "ver pendientes", "pendientes"]:
        st.subheader("📋 Tareas Pendientes")

        if len(st.session_state.pendientes) == 0:
            st.info("¡Felicidades! No tienes tareas pendientes.")
        else:
            df_pendientes = pd.DataFrame(
                {
                    "N°": range(1, len(st.session_state.pendientes) + 1),
                    "Tarea Pendiente": st.session_state.pendientes,
                }
            )
            st.dataframe(
                df_pendientes, use_container_width=True, hide_index=True
            )

    elif opcion in ["4", "ver completadas", "completadas"]:
        st.subheader("🎉 Tareas Completadas")

        if len(st.session_state.completadas) == 0:
            st.info("Aún no has completado ninguna tarea.")
        else:
            df_completadas = pd.DataFrame(
                {
                    "N°": range(1, len(st.session_state.completadas) + 1),
                    "Tarea Completada": st.session_state.completadas,
                }
            )
            st.dataframe(
                df_completadas, use_container_width=True, hide_index=True
            )

    elif opcion in ["5", "salir"]:
        st.markdown(
            "<h1 style='text-align: center; color: #FF4B4B;'>que tenga buen dia</h1>",
            unsafe_allow_html=True,
        )

    else:
        st.error(
            "Opción no válida. Por favor ingrese un número del 1 al 5 o el nombre de la opción."
        )