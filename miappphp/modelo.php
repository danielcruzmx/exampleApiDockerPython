<?php
function getTodosLosArticulos()
{

   // Conectar con la base de datos y ejecutar consulta
   $conexion = mysqli_connect('db', 'root', 'passw', 'test');
   $conexion->set_charset("utf8");

   $res = $conexion->query("SELECT cantidad, descripcion, precio FROM articulo");

   // Crear el array de elementos para la capa de la vista

   $articulos = array();
   while($f = $res->fetch_assoc()){
        $articulos[] = $f;
   }

   $conexion->close();

   return $articulos;
}
?>
