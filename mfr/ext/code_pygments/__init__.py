# -*- coding: utf-8 -*-

from mfr import FileHandler, get_file_extension

try:  # requires pygments
    from .render import render_html
    renderers = {
        'html': render_html,
    }
except ImportError:
    renderers = {}

EXTENSIONS = [
    '',
    '.6pl',
    '.6pm',
    '.ASM',
    '.BAS',
    '.C',
    '.CBL',
    '.COB',
    '.CPP',
    '.CPY',
    '.F',
    '.F90',
    '.G',
    '.H',
    '.PRG',
    '.R',
    '.Rd',
    '.Rout',
    '.S',
    #'.[1234567]',
    '.abap',
    '.ada',
    '.adb',
    '.ads',
    '.agda',
    '.ahk',
    '.ahkl',
    '.aj',
    '.als',
    '.apl',
    '.applescript',
    '.arexx',
    '.as',
    '.asax',
    '.ascx',
    '.ashx',
    '.asm',
    '.asmx',
    '.aspx',
    '.asy',
    '.at',
    '.au3',
    '.aux',
    '.awk',
    '.axd',
    '.b',
    '.bas',
    '.bash',
    '.bat',
    '.bb',
    '.befunge',
    '.bf',
    '.bmx',
    '.boo',
    '.bro',
    '.bug',
    '.c',
    '.c++',
    '.c++-objdump',
    '.c-objdump',
    '.cbl',
    '.cc',
    '.cdf',
    '.ceylon',
    '.cf',
    '.cfc',
    '.cfg',
    '.cfm',
    '.cfml',
    '.chai',
    '.chpl',
    '.cirru',
    '.cl',
    '.clay',
    '.clj',
    '.cljs',
    '.cls',
    '.cmake',
    '.cmd',
    '.cob',
    '.coffee',
    '.cp',
    '.cpp',
    '.cpp-objdump',
    '.cpy',
    '.croc',
    '.cry',
    '.cs',
    '.csh',
    '.css',
    '.css.in',
    '.cu',
    '.cuh',
    '.cw',
    '.cxx',
    '.cxx-objdump',
    '.cyp',
    '.cypher',
    '.d',
    '.d-objdump',
    '.darcspatch',
    '.dart',
    '.decls',
    '.def',
    '.dg',
    '.di',
    '.diff',
    '.docker',
    '.dpatch',
    '.dtd',
    '.duby',
    '.duel',
    '.dyl',
    '.dylan',
    '.dylan-console',
    '.e',
    '.ebnf',
    '.ebuild',
    '.ec',
    '.ecl',
    '.eclass',
    '.eh',
    '.el',
    '.eps',
    '.erl',
    '.erl-sh',
    '.es',
    '.escript',
    '.evoque',
    '.ex',
    '.exs',
    '.f',
    '.f90',
    '.factor',
    '.fan',
    '.fancypack',
    '.feature',
    '.fhtml',
    '.flx',
    '.flxh',
    '.frag',
    '.fs',
    '.fsi',
    '.fun',
    '.fy',
    '.g',
    '.gap',
    '.gd',
    '.gdc',
    '.gemspec',
    '.geo',
    '.gi',
    '.go',
    '.golo',
    '.groovy',
    '.gs',
    '.gsp',
    '.gst',
    '.gsx',
    '.h',
    '.h++',
    '.haml',
    '.handlebars',
    '.hbs',
    '.hdp',
    '.hh',
    '.hpp',
    '.hrl',
    '.hs',
    '.htm',
    '.html',
    '.hx',
    '.hxml',
    '.hxsl',
    '.hxx',
    '.hy',
    '.hyb',
    '.i',
    '.i6t',
    '.i7x',
    '.idc',
    '.idr',
    '.ik',
    '.inc',
    '.inf',
    '.ini',
    '.intr',
    '.io',
    '.ipf',
    '.j',
    '.jade',
    '.jag',
    '.java',
    '.jbst',
    '.jl',
    '.js',
    '.js.in',
    '.json',
    '.jsonld',
    '.jsp',
    '.kal',
    '.kid',
    '.kk',
    '.kki',
    '.ksh',
    '.kt',
    '.lagda',
    '.lasso',
    '.lasso[89]',
    '.lcry',
    '.lean',
    '.lgt',
    '.lhs',
    '.lid',
    '.lidr',
    '.liquid',
    '.lisp',
    '.ll',
    '.logtalk',
    '.ls',
    '.lsl',
    '.lsp',
    '.lua',
    '.m',
    '.ma',
    '.mak',
    '.man',
    '.mao',
    '.maql',
    '.mask',
    '.mc',
    '.mhtml',
    '.mi',
    '.mk',
    '.ml',
    '.mli',
    '.mll',
    '.mly',
    '.mm',
    '.mo',
    '.mod',
    '.monkey',
    '.moo',
    '.moon',
    '.mq4',
    '.mq5',
    '.mqh',
    '.msc',
    '.mu',
    '.mxml',
    '.myt',
    '.n',
    '.nb',
    '.nbp',
    '.nc',
    '.ni',
    '.nim',
    '.nimrod',
    '.nit',
    '.nix',
    '.nl',
    '.nqp',
    '.ns2',
    '.nsh',
    '.nsi',
    '.objdump',
    '.objdump-intel',
    '.ooc',
    '.opa',
    '.p',
    '.p6',
    '.p6l',
    '.p6m',
    '.pan',
    '.pas',
    '.patch',
    '.php',
    '.php[345]',
    '.phtml',
    '.pig',
    '.pike',
    '.pl',
    '.pl6',
    '.plot',
    '.plt',
    '.pm',
    '.pm6',
    '.pmod',
    '.po',
    '.pot',
    '.pov',
    '.pp',
    '.prg',
    '.pro',
    '.prolog',
    '.properties',
    '.proto',
    '.ps',
    '.ps1',
    '.psm1',
    '.pwn',
    '.pxd',
    '.pxi',
    '.py',
    '.py3tb',
    '.pypylog',
    '.pytb',
    '.pyw',
    '.pyx',
    '.qml',
    '.r',
    '.r3',
    '.rake',
    '.rb',
    '.rbw',
    '.rbx',
    '.reb',
    '.red',
    '.reds',
    '.reg',
    '.rest',
    '.rex',
    '.rexx',
    '.rhtml',
    '.rkt',
    '.rktd',
    '.rktl',
    '.rl',
    '.robot',
    '.rpf',
    '.rq',
    '.rql',
    '.rs',
    '.rsl',
    '.rss',
    '.rst',
    '.rvt',
    '.rx',
    '.s',
    '.sage',
    '.sass',
    '.sc',
    '.scala',
    '.scaml',
    '.sce',
    '.sci',
    '.scm',
    '.scss',
    '.sh',
    '.sh-session',
    '.shell-session',
    '.sig',
    '.slim',
    '.sls',
    '.smali',
    '.sml',
    '.snobol',
    '.sp',
    '.sparql',
    '.spec',
    '.spt',
    '.sql',
    '.sqlite3-console',
    '.ss',
    '.ssp',
    '.st',
    '.stan',
    '.sv',
    '.svh',
    '.swg',
    '.swift',
    '.t',
    '.tac',
    '.tcl',
    '.tcsh',
    '.tea',
    '.tex',
    '.thy',
    '.tmpl',
    '.toc',
    '.todotxt',
    '.tpl',
    '.treetop',
    '.ts',
    '.tst',
    '.tt',
    '.twig',
    '.txt',
    '.md',
    '.u',
    '.v',
    '.vala',
    '.vapi',
    '.vark',
    '.vb',
    '.vert',
    '.vhd',
    '.vhdl',
    '.vim',
    '.vm',
    '.weechatlog',
    '.wlua',
    '.wsdl',
    '.wsf',
    '.x',
    '.xhtml',
    '.xi',
    '.xm',
    '.xmi',
    '.xml',
    '.xpl',
    '.xq',
    '.xql',
    '.xqm',
    '.xquery',
    '.xqy',
    '.xsd',
    '.xsl',
    '.xslt',
    '.xtend',
    '.xul.in',
    '.yaml',
    '.yml',
    '.zep',
    #'*Config.in*',
    '.Renviron',
    '.Rhistory',
    '.Rprofile',
    #'.bash_*',
    '.bashrc',
    '.exrc',
    '.gvimrc',
    '.htaccess',
    '.vimrc',
    #'CMakeLists.txt',
    #'Dockerfile',
    #'GNUmakefile',
    #'Kconfig',
    #'Makefile',
    #'Makefile.*',
    #'PKGBUILD',
    #'Rakefile',
    #'SConscript',
    #'SConstruct',
    #'_exrc',
    #'_gvimrc',
    #'_vimrc',
    #'apache.conf',
    #'apache2.conf',
    #'autodelegate',
    #'autohandler',
    #'bash_*',
    #'bashrc',
    #'control',
    #'dhandler',
    #'external.in*',
    #'gvimrc',
    #'makefile',
    #'sources.list',
    #'squid.conf',
    #'standard-modules.in',
    #'todo.txt',
    #'vimrc'
]


class Handler(FileHandler):
    """FileHandler for code files."""
    renderers = renderers

    def detect(self, fp):
        return get_file_extension(fp.name) in EXTENSIONS
