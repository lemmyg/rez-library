set(TBB_INCLUDE_DIR $ENV{REZ_TBB_ROOT}/include)
set(TBB_LIBRARY_DIR $ENV{REZ_TBB_ROOT}/lib)
set(TBB_LIBRARIES ${TBB_LIBRARY_DIR}/libtbb.dylib ${TBB_LIBRARY_DIR}/libtbbmalloc_proxy.dylib ${TBB_LIBRARY_DIR}/libtbbmalloc.dylib)