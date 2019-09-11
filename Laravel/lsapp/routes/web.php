<?php

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

Route::get('/', 'PagesController@index');

Route::get('/services', 'PagesController@services');

Route::get('/hello', function () {
    return 'Hello World';
});

Route::get('/users/{name}', function ($name) {
    return 'This is user: '.$name;
});
