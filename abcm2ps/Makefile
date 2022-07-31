# Makefile source for abcm2ps

CC = gcc
INSTALL = /usr/bin/install -c
INSTALL_DATA = ${INSTALL} -m 644
INSTALL_PROGRAM = ${INSTALL}

CPPFLAGS =  -I.
CFLAGS = -g -O2 -Wall -pipe 
LDFLAGS = 
LDLIBS =  -lm

prefix = /usr/local
exec_prefix = ${prefix}

srcdir = .
VPATH = .

bindir = $(DESTDIR)${exec_prefix}/bin
datadir = $(DESTDIR)${prefix}/share
docdir = $(DESTDIR)${prefix}/share/doc
mandir = $(DESTDIR)${prefix}/share/man

build: abcm2ps abcm2ps.1

# unix
OBJECTS=abcm2ps.o \
	abcparse.o buffer.o deco.o draw.o format.o front.o glyph.o music.o parse.o \
	subs.o svg.o syms.o
abcm2ps: $(OBJECTS)

$(OBJECTS): abcm2ps.h config.h Makefile

abcm2ps.1: abcm2ps.rst
	if [ -x "$$(command -v rst2man)" ]; then\
		rst2man $< $@;\
	else\
		cp $< $@;\
	fi

install: build
	mkdir -p $(bindir)
	$(INSTALL_PROGRAM) abcm2ps $(bindir)
	mkdir -p $(datadir)/abcm2ps
	$(INSTALL_DATA) $(srcdir)/abc2svg.ttf $(datadir)/abcm2ps
	$(INSTALL_DATA) $(srcdir)/*.fmt       $(datadir)/abcm2ps
	mkdir -p $(docdir)/abcm2ps/examples
	$(INSTALL_DATA) $(srcdir)/README.md $(docdir)/abcm2ps
	$(INSTALL_DATA) $(srcdir)/*.abc     $(docdir)/abcm2ps/examples
	$(INSTALL_DATA) $(srcdir)/*.eps     $(docdir)/abcm2ps/examples
	$(INSTALL_DATA) $(srcdir)/*.html    $(docdir)/abcm2ps/examples
	mkdir -p $(mandir)/man1
	$(INSTALL_DATA) abcm2ps.1 $(mandir)/man1

uninstall:
	echo "uninstalling..."
	rm -f  $(bindir)/abcm2ps
	rm -fr $(datadir)/abcm2ps
	rm -fr $(docdir)/abcm2ps
	rm -f  $(mandir)/man1/abcm2ps.1

EXAMPLES = accordion.ps \
	chinese.ps \
	deco.ps \
	newfeatures.ps \
	sample.ps \
	sample2.ps \
	sample3.ps \
	sample4.ps \
	sample5.ps \
	voices.ps

test:	$(EXAMPLES)
%.ps: %.abc
	./abcm2ps -O $@ $<

mostlyclean:
	rm -f *.o $(EXAMPLES)
clean: mostlyclean
	rm -f abcm2ps abcm2ps.1
distclean: clean
	rm -f config.h Makefile
