<html>
   <head>
      <title>Listado de Articulos</title>
   </head>
   <body>
      <h1>Listado de Articulos</h1>
      <table border="1">
         <tr><th>Cantidad</th><th>Descripcion</th><th>Precio</th></tr>
         <?php foreach ($articulos as $articulo): ?>
         <tr>
            <td><?php echo $articulo['cantidad'] ?></td>
            <td><?php echo $articulo['descripcion'] ?></td>
            <td><?php echo $articulo['precio'] ?></td>
         </tr>
         <?php endforeach; ?>
      </table>
   </body>
</html>
