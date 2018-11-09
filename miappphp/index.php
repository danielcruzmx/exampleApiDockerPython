<?php

   // Incluir la logica del modelo
   include('modelo.php');

   // Obtener la lista de articulos
   $articulos = getTodosLosArticulos();

   // Incluir la logica de la vista
   include('vista.php');

?>