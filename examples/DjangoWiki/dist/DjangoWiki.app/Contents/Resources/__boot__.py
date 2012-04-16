def _site_packages():
    import site, sys, os
    paths = []
    prefixes = [sys.prefix]
    if sys.exec_prefix != sys.prefix:
        prefixes.append(sys.exec_prefix)
    for prefix in prefixes:
        paths.append(os.path.join(prefix, 'lib', 'python' + sys.version[:3],
            'site-packages'))
    if os.path.join('.framework', '') in os.path.join(sys.prefix, ''):
        home = os.environ.get('HOME')
        if home:
            paths.append(os.path.join(home, 'Library', 'Python',
                sys.version[:3], 'site-packages'))
    for path in paths:
        site.addsitedir(path)
_site_packages()


def _chdir_resource():
    import os
    os.chdir(os.environ['RESOURCEPATH'])
_chdir_resource()


def _path_inject(paths):
    import sys
    sys.path[:0] = paths


_path_inject(['/Users/tomi/svn/Projects/DjangoKit/djangokit'])


def _run(*scripts):
    global __file__
    import os, sys, site
    import Carbon.File
    sys.frozen = 'macosx_app'
    site.addsitedir(os.environ['RESOURCEPATH'])
    for (script, path) in scripts:
        alias = Carbon.File.Alias(rawdata=script)
        target, wasChanged = alias.ResolveAlias(None)
        if not os.path.exists(path):
            path = target.as_pathname()
        sys.path.append(os.path.dirname(path))
        sys.argv[0] = __file__ = path
        execfile(path, globals(), globals())


try:
    _run(('\x00\x00\x00\x00\x00\xd6\x00\x02\x00\x00\x06Sartre\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\xc1\xe6\x9c2H+\x00\x00\x00/\xd1J\x06app.py\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x000.\x92\xc2D\x11\xf7TEXT\x00\x00\x00\x00\xff\xff\xff\xff\x00\x00\t \x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x10\x00\x08\x00\x00\xc1\xe6\xf0\x92\x00\x00\x00\x11\x00\x08\x00\x00\xc2DXG\x00\x00\x00\x0e\x00\x0e\x00\x06\x00a\x00p\x00p\x00.\x00p\x00y\x00\x0f\x00\x0e\x00\x06\x00S\x00a\x00r\x00t\x00r\x00e\xff\xff\x00\x00', '/Users/tomi/svn/Projects/DjangoKit/djangokit/app.py'))
except KeyboardInterrupt:
    pass
