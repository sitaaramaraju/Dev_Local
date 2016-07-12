<?php
$data = implode ( ',', $_POST );
print_r ( json_encode ( array ('result' => $data ) ) );
exit ();
