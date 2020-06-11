#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xDBD2CE893E2D1C87 (cfeck@kde.org)
#
Name     : khelpcenter
Version  : 20.04.2
Release  : 22
URL      : https://download.kde.org/stable/release-service/20.04.2/src/khelpcenter-20.04.2.tar.xz
Source0  : https://download.kde.org/stable/release-service/20.04.2/src/khelpcenter-20.04.2.tar.xz
Source1  : https://download.kde.org/stable/release-service/20.04.2/src/khelpcenter-20.04.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: khelpcenter-bin = %{version}-%{release}
Requires: khelpcenter-data = %{version}-%{release}
Requires: khelpcenter-lib = %{version}-%{release}
Requires: khelpcenter-license = %{version}-%{release}
Requires: khelpcenter-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : grantlee-dev
BuildRequires : khtml-dev
BuildRequires : kjs-dev
BuildRequires : libxml2-dev
BuildRequires : xapian-core-dev

%description
KHelpCenter documentation meta data structure
=============================================

%package bin
Summary: bin components for the khelpcenter package.
Group: Binaries
Requires: khelpcenter-data = %{version}-%{release}
Requires: khelpcenter-license = %{version}-%{release}

%description bin
bin components for the khelpcenter package.


%package data
Summary: data components for the khelpcenter package.
Group: Data

%description data
data components for the khelpcenter package.


%package doc
Summary: doc components for the khelpcenter package.
Group: Documentation

%description doc
doc components for the khelpcenter package.


%package lib
Summary: lib components for the khelpcenter package.
Group: Libraries
Requires: khelpcenter-data = %{version}-%{release}
Requires: khelpcenter-license = %{version}-%{release}

%description lib
lib components for the khelpcenter package.


%package license
Summary: license components for the khelpcenter package.
Group: Default

%description license
license components for the khelpcenter package.


%package locales
Summary: locales components for the khelpcenter package.
Group: Default

%description locales
locales components for the khelpcenter package.


%prep
%setup -q -n khelpcenter-20.04.2
cd %{_builddir}/khelpcenter-20.04.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1591902288
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%cmake ..
make  %{?_smp_mflags}  VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1591902288
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/khelpcenter
cp %{_builddir}/khelpcenter-20.04.2/COPYING %{buildroot}/usr/share/package-licenses/khelpcenter/8cf4afb0636055f7cacd1b6955e0e8ebec7888f5
pushd clr-build
%make_install
popd
%find_lang khelpcenter5

%files
%defattr(-,root,root,-)
/usr/lib64/libexec/khc_mansearch.pl
/usr/lib64/libexec/khc_xapianindexer
/usr/lib64/libexec/khc_xapiansearch

%files bin
%defattr(-,root,root,-)
/usr/bin/khelpcenter

%files data
%defattr(-,root,root,-)
/usr/share/applications/org.kde.Help.desktop
/usr/share/config.kcfg/khelpcenter.kcfg
/usr/share/kde4/services/khelpcenter.desktop
/usr/share/khelpcenter/glossary.xslt
/usr/share/khelpcenter/plugins/Applications/.directory
/usr/share/khelpcenter/plugins/Manpages/.directory
/usr/share/khelpcenter/plugins/Manpages/man1.desktop
/usr/share/khelpcenter/plugins/Manpages/man2.desktop
/usr/share/khelpcenter/plugins/Manpages/man3.desktop
/usr/share/khelpcenter/plugins/Manpages/man4.desktop
/usr/share/khelpcenter/plugins/Manpages/man5.desktop
/usr/share/khelpcenter/plugins/Manpages/man6.desktop
/usr/share/khelpcenter/plugins/Manpages/man7.desktop
/usr/share/khelpcenter/plugins/Manpages/man8.desktop
/usr/share/khelpcenter/plugins/Scrollkeeper/.directory
/usr/share/khelpcenter/plugins/browsercontrolmodules.desktop
/usr/share/khelpcenter/plugins/filemanagercontrolmodules.desktop
/usr/share/khelpcenter/plugins/fundamentals.desktop
/usr/share/khelpcenter/plugins/info.desktop
/usr/share/khelpcenter/plugins/kcontrolmodules.desktop
/usr/share/khelpcenter/plugins/kicmodules.desktop
/usr/share/khelpcenter/plugins/kioslaves.desktop
/usr/share/khelpcenter/plugins/konquerorcontrolmodules.desktop
/usr/share/khelpcenter/plugins/onlinehelp.desktop
/usr/share/khelpcenter/plugins/othercontrolmodules.desktop
/usr/share/khelpcenter/plugins/plasma.desktop
/usr/share/khelpcenter/searchhandlers/man.desktop
/usr/share/khelpcenter/searchhandlers/xapian.desktop
/usr/share/khelpcenter/table-of-contents.xslt
/usr/share/khelpcenter/templates/glossary.html
/usr/share/khelpcenter/templates/index.html
/usr/share/khelpcenter/templates/search.html
/usr/share/kservices5/khelpcenter.desktop
/usr/share/kxmlgui5/khelpcenter/khelpcenterui.rc
/usr/share/metainfo/org.kde.Help.appdata.xml
/usr/share/qlogging-categories5/khelpcenter.categories

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/HTML/ca/fundamentals/colors.png
/usr/share/doc/HTML/ca/fundamentals/config.docbook
/usr/share/doc/HTML/ca/fundamentals/files-locationbar-breadcrumb.png
/usr/share/doc/HTML/ca/fundamentals/files-locationbar-context-menu.png
/usr/share/doc/HTML/ca/fundamentals/files-locationbar-editable.png
/usr/share/doc/HTML/ca/fundamentals/files-locationbar-places-icon.png
/usr/share/doc/HTML/ca/fundamentals/files-open.png
/usr/share/doc/HTML/ca/fundamentals/files-save.png
/usr/share/doc/HTML/ca/fundamentals/find-find-inline.png
/usr/share/doc/HTML/ca/fundamentals/find-replace-inline.png
/usr/share/doc/HTML/ca/fundamentals/fonts.png
/usr/share/doc/HTML/ca/fundamentals/index.cache.bz2
/usr/share/doc/HTML/ca/fundamentals/index.docbook
/usr/share/doc/HTML/ca/fundamentals/install.docbook
/usr/share/doc/HTML/ca/fundamentals/menus.png
/usr/share/doc/HTML/ca/fundamentals/shortcuts-schemes.png
/usr/share/doc/HTML/ca/fundamentals/shortcuts-set.png
/usr/share/doc/HTML/ca/fundamentals/tasks.docbook
/usr/share/doc/HTML/ca/fundamentals/toolbars-configure.png
/usr/share/doc/HTML/ca/fundamentals/toolbars-toolbar.png
/usr/share/doc/HTML/ca/fundamentals/ui.docbook
/usr/share/doc/HTML/ca/fundamentals/visualdict-breadcrumb.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-button.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-central-widget.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-check-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-color-selector.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-combo-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-context-menu.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-dialog-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-drop-down-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-icon.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-list-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-panel.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-progress-bar.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-radio-button.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-scrollbar.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-slider.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-spin-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-text-area.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-text-box.png
/usr/share/doc/HTML/ca/fundamentals/visualdict-toolbar.png
/usr/share/doc/HTML/ca/khelpcenter/background.png
/usr/share/doc/HTML/ca/khelpcenter/bgtable.png
/usr/share/doc/HTML/ca/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/ca/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/ca/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/ca/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/ca/khelpcenter/index.docbook
/usr/share/doc/HTML/ca/khelpcenter/kdelogo2.png
/usr/share/doc/HTML/ca/khelpcenter/khelpcenter.png
/usr/share/doc/HTML/ca/khelpcenter/lines.png
/usr/share/doc/HTML/ca/khelpcenter/lines2.png
/usr/share/doc/HTML/ca/khelpcenter/pointers.png
/usr/share/doc/HTML/ca/khelpcenter/shadow1.png
/usr/share/doc/HTML/ca/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/ca/onlinehelp/index.docbook
/usr/share/doc/HTML/de/fundamentals/config.docbook
/usr/share/doc/HTML/de/fundamentals/index.cache.bz2
/usr/share/doc/HTML/de/fundamentals/index.docbook
/usr/share/doc/HTML/de/fundamentals/install.docbook
/usr/share/doc/HTML/de/fundamentals/tasks.docbook
/usr/share/doc/HTML/de/fundamentals/ui.docbook
/usr/share/doc/HTML/de/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/de/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/de/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/de/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/de/khelpcenter/index.docbook
/usr/share/doc/HTML/de/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/de/onlinehelp/index.docbook
/usr/share/doc/HTML/en/fundamentals/colors.png
/usr/share/doc/HTML/en/fundamentals/config.docbook
/usr/share/doc/HTML/en/fundamentals/files-locationbar-breadcrumb.png
/usr/share/doc/HTML/en/fundamentals/files-locationbar-context-menu.png
/usr/share/doc/HTML/en/fundamentals/files-locationbar-editable.png
/usr/share/doc/HTML/en/fundamentals/files-locationbar-places-icon.png
/usr/share/doc/HTML/en/fundamentals/files-open.png
/usr/share/doc/HTML/en/fundamentals/files-save.png
/usr/share/doc/HTML/en/fundamentals/find-find-inline.png
/usr/share/doc/HTML/en/fundamentals/find-find.png
/usr/share/doc/HTML/en/fundamentals/find-found.png
/usr/share/doc/HTML/en/fundamentals/find-replace-inline.png
/usr/share/doc/HTML/en/fundamentals/find-replace.png
/usr/share/doc/HTML/en/fundamentals/fonts.png
/usr/share/doc/HTML/en/fundamentals/index.cache.bz2
/usr/share/doc/HTML/en/fundamentals/index.docbook
/usr/share/doc/HTML/en/fundamentals/install.docbook
/usr/share/doc/HTML/en/fundamentals/menus.png
/usr/share/doc/HTML/en/fundamentals/shortcuts-schemes.png
/usr/share/doc/HTML/en/fundamentals/shortcuts-search.png
/usr/share/doc/HTML/en/fundamentals/shortcuts-set.png
/usr/share/doc/HTML/en/fundamentals/spellcheck-check.png
/usr/share/doc/HTML/en/fundamentals/tasks.docbook
/usr/share/doc/HTML/en/fundamentals/toolbars-configure.png
/usr/share/doc/HTML/en/fundamentals/toolbars-toolbar.png
/usr/share/doc/HTML/en/fundamentals/ui.docbook
/usr/share/doc/HTML/en/fundamentals/visualdict-breadcrumb.png
/usr/share/doc/HTML/en/fundamentals/visualdict-button.png
/usr/share/doc/HTML/en/fundamentals/visualdict-central-widget.png
/usr/share/doc/HTML/en/fundamentals/visualdict-check-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-color-selector.png
/usr/share/doc/HTML/en/fundamentals/visualdict-combo-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-context-menu.png
/usr/share/doc/HTML/en/fundamentals/visualdict-dialog-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-drop-down-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-gui1.png
/usr/share/doc/HTML/en/fundamentals/visualdict-gui2.png
/usr/share/doc/HTML/en/fundamentals/visualdict-gui3.png
/usr/share/doc/HTML/en/fundamentals/visualdict-gui4.png
/usr/share/doc/HTML/en/fundamentals/visualdict-icon-list.png
/usr/share/doc/HTML/en/fundamentals/visualdict-icon.png
/usr/share/doc/HTML/en/fundamentals/visualdict-list-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-menu-button.png
/usr/share/doc/HTML/en/fundamentals/visualdict-menu.png
/usr/share/doc/HTML/en/fundamentals/visualdict-menubar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-panel.png
/usr/share/doc/HTML/en/fundamentals/visualdict-progress-bar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-radio-button.png
/usr/share/doc/HTML/en/fundamentals/visualdict-scrollbar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-slider.png
/usr/share/doc/HTML/en/fundamentals/visualdict-spin-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-statusbar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-tab.png
/usr/share/doc/HTML/en/fundamentals/visualdict-text-area.png
/usr/share/doc/HTML/en/fundamentals/visualdict-text-box.png
/usr/share/doc/HTML/en/fundamentals/visualdict-titlebar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-toolbar.png
/usr/share/doc/HTML/en/fundamentals/visualdict-tree-view.png
/usr/share/doc/HTML/en/fundamentals/visualdict-window.png
/usr/share/doc/HTML/en/fundamentals/visualdict-window2.png
/usr/share/doc/HTML/en/khelpcenter/background.png
/usr/share/doc/HTML/en/khelpcenter/bgtable.png
/usr/share/doc/HTML/en/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/en/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/en/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/en/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/en/khelpcenter/index.docbook
/usr/share/doc/HTML/en/khelpcenter/kdelogo2.png
/usr/share/doc/HTML/en/khelpcenter/khelpcenter.png
/usr/share/doc/HTML/en/khelpcenter/lines.png
/usr/share/doc/HTML/en/khelpcenter/lines2.png
/usr/share/doc/HTML/en/khelpcenter/pointers.png
/usr/share/doc/HTML/en/khelpcenter/shadow1.png
/usr/share/doc/HTML/en/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/en/onlinehelp/index.docbook
/usr/share/doc/HTML/es/fundamentals/config.docbook
/usr/share/doc/HTML/es/fundamentals/index.cache.bz2
/usr/share/doc/HTML/es/fundamentals/index.docbook
/usr/share/doc/HTML/es/fundamentals/install.docbook
/usr/share/doc/HTML/es/fundamentals/tasks.docbook
/usr/share/doc/HTML/es/fundamentals/ui.docbook
/usr/share/doc/HTML/es/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/es/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/es/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/es/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/es/khelpcenter/index.docbook
/usr/share/doc/HTML/es/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/es/onlinehelp/index.docbook
/usr/share/doc/HTML/it/fundamentals/config.docbook
/usr/share/doc/HTML/it/fundamentals/index.cache.bz2
/usr/share/doc/HTML/it/fundamentals/index.docbook
/usr/share/doc/HTML/it/fundamentals/install.docbook
/usr/share/doc/HTML/it/fundamentals/tasks.docbook
/usr/share/doc/HTML/it/fundamentals/ui.docbook
/usr/share/doc/HTML/it/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/it/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/it/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/it/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/it/khelpcenter/index.docbook
/usr/share/doc/HTML/it/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/it/onlinehelp/index.docbook
/usr/share/doc/HTML/nl/fundamentals/config.docbook
/usr/share/doc/HTML/nl/fundamentals/index.cache.bz2
/usr/share/doc/HTML/nl/fundamentals/index.docbook
/usr/share/doc/HTML/nl/fundamentals/install.docbook
/usr/share/doc/HTML/nl/fundamentals/tasks.docbook
/usr/share/doc/HTML/nl/fundamentals/ui.docbook
/usr/share/doc/HTML/nl/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/nl/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/nl/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/nl/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/nl/khelpcenter/index.docbook
/usr/share/doc/HTML/nl/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/nl/onlinehelp/index.docbook
/usr/share/doc/HTML/pt/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/pt/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/pt/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/config.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/files-locationbar-breadcrumb.png
/usr/share/doc/HTML/pt_BR/fundamentals/files-locationbar-context-menu.png
/usr/share/doc/HTML/pt_BR/fundamentals/files-locationbar-editable.png
/usr/share/doc/HTML/pt_BR/fundamentals/files-locationbar-places-icon.png
/usr/share/doc/HTML/pt_BR/fundamentals/files-open.png
/usr/share/doc/HTML/pt_BR/fundamentals/files-save.png
/usr/share/doc/HTML/pt_BR/fundamentals/find-find-inline.png
/usr/share/doc/HTML/pt_BR/fundamentals/find-find.png
/usr/share/doc/HTML/pt_BR/fundamentals/find-found.png
/usr/share/doc/HTML/pt_BR/fundamentals/find-replace-inline.png
/usr/share/doc/HTML/pt_BR/fundamentals/find-replace.png
/usr/share/doc/HTML/pt_BR/fundamentals/index.cache.bz2
/usr/share/doc/HTML/pt_BR/fundamentals/index.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/install.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/menus.png
/usr/share/doc/HTML/pt_BR/fundamentals/shortcuts-schemes.png
/usr/share/doc/HTML/pt_BR/fundamentals/shortcuts-search.png
/usr/share/doc/HTML/pt_BR/fundamentals/shortcuts-set.png
/usr/share/doc/HTML/pt_BR/fundamentals/tasks.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/toolbars-configure.png
/usr/share/doc/HTML/pt_BR/fundamentals/toolbars-toolbar.png
/usr/share/doc/HTML/pt_BR/fundamentals/ui.docbook
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-breadcrumb.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-button.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-check-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-combo-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-context-menu.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-dialog-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-drop-down-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-icon-list.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-icon.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-list-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-menu-button.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-menu.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-menubar.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-panel.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-radio-button.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-scrollbar.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-slider.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-spin-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-statusbar.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-tab.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-text-box.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-titlebar.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-toolbar.png
/usr/share/doc/HTML/pt_BR/fundamentals/visualdict-tree-view.png
/usr/share/doc/HTML/pt_BR/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/pt_BR/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/pt_BR/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/pt_BR/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/pt_BR/khelpcenter/index.docbook
/usr/share/doc/HTML/pt_BR/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/pt_BR/onlinehelp/index.docbook
/usr/share/doc/HTML/ru/fundamentals/colors.png
/usr/share/doc/HTML/ru/fundamentals/config.docbook
/usr/share/doc/HTML/ru/fundamentals/files-locationbar-breadcrumb.png
/usr/share/doc/HTML/ru/fundamentals/files-locationbar-context-menu.png
/usr/share/doc/HTML/ru/fundamentals/files-locationbar-editable.png
/usr/share/doc/HTML/ru/fundamentals/files-locationbar-places-icon.png
/usr/share/doc/HTML/ru/fundamentals/files-open.png
/usr/share/doc/HTML/ru/fundamentals/find-find-inline.png
/usr/share/doc/HTML/ru/fundamentals/find-find.png
/usr/share/doc/HTML/ru/fundamentals/find-found.png
/usr/share/doc/HTML/ru/fundamentals/find-replace-inline.png
/usr/share/doc/HTML/ru/fundamentals/find-replace.png
/usr/share/doc/HTML/ru/fundamentals/fonts.png
/usr/share/doc/HTML/ru/fundamentals/index.cache.bz2
/usr/share/doc/HTML/ru/fundamentals/index.docbook
/usr/share/doc/HTML/ru/fundamentals/install.docbook
/usr/share/doc/HTML/ru/fundamentals/menus.png
/usr/share/doc/HTML/ru/fundamentals/shortcuts-schemes.png
/usr/share/doc/HTML/ru/fundamentals/shortcuts-search.png
/usr/share/doc/HTML/ru/fundamentals/shortcuts-set.png
/usr/share/doc/HTML/ru/fundamentals/spellcheck-check.png
/usr/share/doc/HTML/ru/fundamentals/tasks.docbook
/usr/share/doc/HTML/ru/fundamentals/toolbars-configure.png
/usr/share/doc/HTML/ru/fundamentals/toolbars-toolbar.png
/usr/share/doc/HTML/ru/fundamentals/ui.docbook
/usr/share/doc/HTML/ru/fundamentals/visualdict-breadcrumb.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-button.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-central-widget.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-check-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-color-selector.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-combo-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-context-menu.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-dialog-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-drop-down-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-gui1.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-gui2.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-gui3.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-icon-list.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-icon.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-list-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-menu-button.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-menu.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-menubar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-panel.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-progress-bar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-radio-button.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-scrollbar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-slider.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-spin-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-statusbar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-tab.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-text-area.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-text-box.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-titlebar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-toolbar.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-tree-view.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-window.png
/usr/share/doc/HTML/ru/fundamentals/visualdict-window2.png
/usr/share/doc/HTML/ru/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/ru/khelpcenter/index.docbook
/usr/share/doc/HTML/ru/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/ru/onlinehelp/index.docbook
/usr/share/doc/HTML/sr/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/sr/khelpcenter/index.docbook
/usr/share/doc/HTML/sr/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/sr/onlinehelp/index.docbook
/usr/share/doc/HTML/sv/fundamentals/config.docbook
/usr/share/doc/HTML/sv/fundamentals/index.cache.bz2
/usr/share/doc/HTML/sv/fundamentals/index.docbook
/usr/share/doc/HTML/sv/fundamentals/install.docbook
/usr/share/doc/HTML/sv/fundamentals/tasks.docbook
/usr/share/doc/HTML/sv/fundamentals/ui.docbook
/usr/share/doc/HTML/sv/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/sv/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/sv/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/sv/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/sv/khelpcenter/index.docbook
/usr/share/doc/HTML/sv/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/sv/onlinehelp/index.docbook
/usr/share/doc/HTML/uk/fundamentals/colors.png
/usr/share/doc/HTML/uk/fundamentals/config.docbook
/usr/share/doc/HTML/uk/fundamentals/files-locationbar-breadcrumb.png
/usr/share/doc/HTML/uk/fundamentals/files-locationbar-context-menu.png
/usr/share/doc/HTML/uk/fundamentals/files-locationbar-editable.png
/usr/share/doc/HTML/uk/fundamentals/files-locationbar-places-icon.png
/usr/share/doc/HTML/uk/fundamentals/files-open.png
/usr/share/doc/HTML/uk/fundamentals/files-save.png
/usr/share/doc/HTML/uk/fundamentals/find-find-inline.png
/usr/share/doc/HTML/uk/fundamentals/find-find.png
/usr/share/doc/HTML/uk/fundamentals/find-found.png
/usr/share/doc/HTML/uk/fundamentals/find-replace-inline.png
/usr/share/doc/HTML/uk/fundamentals/find-replace.png
/usr/share/doc/HTML/uk/fundamentals/fonts.png
/usr/share/doc/HTML/uk/fundamentals/index.cache.bz2
/usr/share/doc/HTML/uk/fundamentals/index.docbook
/usr/share/doc/HTML/uk/fundamentals/install.docbook
/usr/share/doc/HTML/uk/fundamentals/menus.png
/usr/share/doc/HTML/uk/fundamentals/shortcuts-schemes.png
/usr/share/doc/HTML/uk/fundamentals/shortcuts-search.png
/usr/share/doc/HTML/uk/fundamentals/shortcuts-set.png
/usr/share/doc/HTML/uk/fundamentals/spellcheck-check.png
/usr/share/doc/HTML/uk/fundamentals/tasks.docbook
/usr/share/doc/HTML/uk/fundamentals/toolbars-configure.png
/usr/share/doc/HTML/uk/fundamentals/ui.docbook
/usr/share/doc/HTML/uk/khelpcenter/glossary/index.cache.bz2
/usr/share/doc/HTML/uk/khelpcenter/glossary/index.docbook
/usr/share/doc/HTML/uk/khelpcenter/glossary/kdeprintingglossary.docbook
/usr/share/doc/HTML/uk/khelpcenter/index.cache.bz2
/usr/share/doc/HTML/uk/khelpcenter/index.docbook
/usr/share/doc/HTML/uk/onlinehelp/index.cache.bz2
/usr/share/doc/HTML/uk/onlinehelp/index.docbook

%files lib
%defattr(-,root,root,-)
/usr/lib64/libkdeinit5_khelpcenter.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/khelpcenter/8cf4afb0636055f7cacd1b6955e0e8ebec7888f5

%files locales -f khelpcenter5.lang
%defattr(-,root,root,-)

