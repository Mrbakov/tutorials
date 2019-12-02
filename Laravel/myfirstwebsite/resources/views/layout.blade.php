<!DOCTYPE html>
<html>

<head>

<body>
    <header>
        <meta name="csrf-token" content="{{ csrf_token() }}">
        <div class="container">
            @yield('content')
        </div>
    </header>
</body>
</head>

</html>