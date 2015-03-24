//# pytablerow.cc: python module for TableRowProxy object.
//# Copyright (C) 2006
//# Associated Universities, Inc. Washington DC, USA.
//#
//# This library is free software; you can redistribute it and/or modify it
//# under the terms of the GNU Library General Public License as published by
//# the Free Software Foundation; either version 2 of the License, or (at your
//# option) any later version.
//#
//# This library is distributed in the hope that it will be useful, but WITHOUT
//# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
//# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
//# License for more details.
//#
//# You should have received a copy of the GNU Library General Public License
//# along with this library; if not, write to the Free Software Foundation,
//# Inc., 675 Massachusetts Ave, Cambridge, MA 02139, USA.
//#
//# Correspondence concerning AIPS++ should be addressed as follows:
//#        Internet email: aips2-request@nrao.edu.
//#        Postal address: AIPS++ Project Office
//#                        National Radio Astronomy Observatory
//#                        520 Edgemont Road
//#                        Charlottesville, VA 22903-2475 USA
//#
//# $Id: pytablerow.cc,v 1.2 2006/10/25 22:14:54 gvandiep Exp $

#include <tables/Tables/TableRowProxy.h>
#include <tables/Tables/TableProxy.h>
#include <pyrap/Converters/PycBasicData.h>
#include <pyrap/Converters/PycRecord.h>
#include <boost/python.hpp>
#include <boost/python/args.hpp>

using namespace boost::python;

namespace casa { namespace pyrap {

  void pytablerow()
  {
    class_<TableRowProxy> ("TableRow",
	    init<TableProxy, Vector<String>, Bool>())

      .def ("_iswritable", &TableRowProxy::isWritable)
      .def ("_get", &TableRowProxy::get,
	    (boost::python::arg("rownr")))
      .def ("_put", &TableRowProxy::put,
	    (boost::python::arg("rownr"),
	     boost::python::arg("value"),
	     boost::python::arg("matchingfields")))
      ;
  }
    
}}
