#  Cliente-Servidor con Sockets en Java

##  Descripción General

Este repositorio contiene una implementación clásica de un sistema **Cliente-Servidor** utilizando la API de **Sockets de Java** (`java.net`). El proyecto está diseñado para demostrar los fundamentos de la programación de redes, la comunicación TCP/IP y el manejo de conexiones concurrentes.

La aplicación permite que uno o múltiples clientes se conecten a un servidor central para enviar y recibir mensajes en tiempo real, simulando un servicio de chat básico por consola.

---

## Características Principales

* **Servidor (Server):**
    * Escucha en un puerto específico (`ServerSocket`) esperando conexiones entrantes.
    * **Multi-threading:** Es capaz de manejar múltiples clientes de forma simultánea. Por cada cliente que se conecta, el servidor instancia un nuevo hilo (`Thread` o `Runnable`) para gestionar la comunicación con ese cliente de forma aislada.
* **Cliente (Client):**
    * Se conecta al servidor especificando una dirección IP (ej. `localhost`) y un número de puerto.
    * Permite al usuario enviar mensajes al servidor a través de la consola.
* **Comunicación Bidireccional:**
    * Utiliza `InputStream` y `OutputStream` (probablemente encapsulados en `BufferedReader` y `PrintWriter`) para una comunicación de texto eficiente entre el cliente y el servidor.

---

## 🛠️ Arquitectura y Tecnologías

### Tecnologías Utilizadas

* **Lenguaje:** **Java** (Core)
* **APIs de Red:** **Java Sockets API**
    * `java.net.ServerSocket`: Para la escucha pasiva en el lado del servidor.
    * `java.net.Socket`: Para el punto final de comunicación (usado tanto por el cliente para conectarse como por el servidor para aceptar la conexión).
* **Concurrencia:** **Java Threads** (`java.lang.Thread` o `java.lang.Runnable`) para manejar múltiples clientes en el servidor.

### Estructura del Proyecto

* **`Server.java`:** La clase principal del servidor. Contiene el `main` que inicia el `ServerSocket` y entra en un bucle infinito para aceptar nuevas conexiones de clientes.
* **`Client.java`:** La clase principal del cliente. Contiene el `main` que establece la conexión `Socket` con el servidor e inicializa los flujos (streams) de entrada/salida.
* **`ClientHandler.java` (o similar):** Una clase `Runnable` utilizada por el servidor. Cada instancia de esta clase maneja la lógica de comunicación (leer mensajes y/o retransmitirlos) para un único cliente conectado, permitiendo así la concurrencia.
