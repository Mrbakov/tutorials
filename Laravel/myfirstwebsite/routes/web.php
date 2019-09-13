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

Route::resource('project', 'ProjectsController');

// Route::get('/projects', "ProjectController@index");

// Route::get('/projects/create', "ProjectController@create");

// Route::get('/projects/{id?}', "ProjectController@show");

// Route::post('/projects', "ProjectController@store");

// Route::get('projects/{id?}/edit', "ProjectController@edit");

// Route::patch('projects/{id?}', 'ProjectController@update');

// Route::delete('projects/{id?}', 'ProjectController@destroy');
