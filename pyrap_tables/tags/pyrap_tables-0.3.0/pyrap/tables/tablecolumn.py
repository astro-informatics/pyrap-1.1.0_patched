# tablecolumn.py: Python tablecolumn functions
# Copyright (C) 2006
# Associated Universities, Inc. Washington DC, USA.
#
# This library is free software; you can redistribute it and/or modify it
# under the terms of the GNU Library General Public License as published by
# the Free Software Foundation; either version 2 of the License, or (at your
# option) any later version.
#
# This library is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE.  See the GNU Library General Public
# License for more details.
#
# You should have received a copy of the GNU Library General Public License
# along with this library; if not, write to the Free Software Foundation,
# Inc., 675 Massachusetts Ave, Cambridge, MA 02139, USA.
#
# Correspondence concerning AIPS++ should be addressed as follows:
#        Internet email: aips2-request@nrao.edu.
#        Postal address: AIPS++ Project Office
#                        National Radio Astronomy Observatory
#                        520 Edgemont Road
#                        Charlottesville, VA 22903-2475 USA
#
# $Id: tablecolumn.py,v 1.9 2007/08/28 07:22:18 gvandiep Exp $

class tablecolumn:
    """The Python interface to a column in a Casacore table.

    The `tablecolumn` class is a convenience class to access data in a
    table column. All functionality provided in this class is available in
    :class:`table`, but `tablecolumn` is more convenient to use because the
    column name does not have to be given over and over again.

    For example::

      t = table('3C343.MS')
      tc = tablecolumn(t, 'DATA')
      # tc = t.col('DATA')           # another way to construct a tablecolumn
      tc.getcell(0)                  # get data from cell 0

    As can be seen in the example :func:`table.col` offers a slightly more
    convenient way to create a `tablecolumn` object.

    A `tablecolumn` can be indexed using Python's [] operator. Negative start,
    end, and stride is possible. For example::

      tc[0]               # get cell 0
      tc[:5]              # get cell 0,1,2,3,4
      tc[-5,-1,]          # get last 4 cells
      tc[-1,-5,-1]        # get last 4 cells in reversed order
      tc[1] = tr[0]       # put value of cell 0 into cell 1

    """

    def __init__(self, table, columnname):
        if not columnname in table.colnames():
            raise RuntimeError("Column " + columnname + " does not exist in table " + table.name());
        self._table  = table;
        self._column = columnname;

    def name (self):
        """Get the name of the column."""
        return self._column;

    def table (self):
        """Get the table object this column belongs to."""
        return self._table;

    def isscalar (self):
        """Tell if the column contains scalar values."""
        return self._table.isscalarcol (self._column);

    def isvar (self):
        """Tell if the column holds variable shaped arrays."""
        return self._table.isvarcol (self._column);

    def datatype (self):
        """Get the data type of the column.
        (see :func:`table.coldatatype`)"""
        return self._table.coldatatype (self._column);

    def arraytype (self):
        """Get the array type of a column holding arrays.
        (see :func:`table.colarraytype`)"""
        return self._table.colarraytype (self._column);

    def nrows (self):
        """Get number of cells in the column."""
        return self._table.nrows();

    def getshapestring (self, startrow=1, nrow=-1, rowincr=1):
        """Get the shapes of all cells in the column in string format.
        (see :func:`table.getcolshapestring`)"""
        return self._table.getcolshapestring (self._column,
                                              startrow, nrow, rowincr);

    def iscelldefined (self, rownr):
        """Tell if a column cell contains a value.
        (see :func:`table.iscelldefined`)"""
        return self._table.iscelldefined (self._column, rownr);

    def getcell (self, rownr):
        """Get data from a column cell.
        (see :func:`table.getcell`)"""
        return self._table.getcell (self._column, rownr);

    def getcellslice (self, rownr, blc, trc, inc=[]):
        """Get a slice from a column cell holding an array.
        (see :func:`table.getcellslice`)"""
        return self._table.getcellslice (self._column, rownr, blc, trc, inc);

    def getcol (self, startrow=0, nrow=-1, rowincr=1):
        """Get the contents of the column or part of it.
        (see :func:`table.getcol`)"""
        return self._table.getcol (self._column, startrow, nrow, rowincr);

    def getvarcol (self, startrow=0, nrow=-1, rowincr=1):
        """Get the contents of the column or part of it.
        (see :func:`table.getvarcol`)"""
        return self._table.getvarcol (self._column, startrow, nrow, rowincr);

    def getcolslice (self, blc, trc, inc=[], startrow=0, nrow=-1, rowincr=1):
        """Get a slice from a table column holding arrays.
        (see :func:`table.getcolslice`)"""
        return self._table.getcolslice (self._column, blc, trc, inc, startrow, nrow, rowincr);

    def putcell (self, rownr, value):
        """Put a value into one or more table cells.
        (see :func:`table.putcell`)"""
        return self._table.putcell (self._column, rownr, value);

    def putcellslice (self, rownr, value, blc, trc, inc=[]):
        """Put into a slice of a table cell holding an array.
        (see :func:`table.putcellslice`)"""
        return self._table.putcellslice (self._column, rownr, value, blc, trc, inc);

    def putcol (self, value, startrow=0, nrow=-1, rowincr=1):
        """Put an entire column or part of it.
        (see :func:`table.putcol`)"""
        return self._table.putcol (self._column, value, startrow, nrow, rowincr);

    def putvarcol (self, value, startrow=0, nrow=-1, rowincr=1):
        """Put an entire column or part of it.
        (see :func:`table.putvarcol`)"""
        return self._table.putvarcol (self._column, value, startrow, nrow, rowincr);

    def putcolslice (self, value, blc, trc, inc=[], startrow=0, nrow=-1, rowincr=1):
        """Put into a slice in a table column holding arrays.
        (see :func:`table.putcolslice`)"""
        return self._table.putcolslice (self._column, value, blc, trc, inc, startrow, nrow, rowincr);

    def keywordnames (self):
        """Get the names of all keywords of the column."""
        return self._table.colkeywordnames (self._column);

    def fieldnames (self, keyword=''):
        """Get the names of the fields in a column keyword value.
        (see :func:`table.colfieldnames`)"""
        return  self._table.colfieldnames (self._column, keyword);

    def getkeyword (self, keyword):
        """Get the value of a column keyword.
        (see :func:`table.getcolkeyword`)"""
        return  self._table.getcolkeyword (self._column, keyword);

    def getkeywords (self):
        """Get the value of all keywords of the column.
        (see :func:`table.getcolkeywords`)"""
        return self._table.getcolkeywords (self._column);

    def putkeyword (self, keyword, value, makesubrecord=False):
        """Put the value of a column keyword.
        (see :func:`table.putcolkeyword`)"""
        return self._table.putcolkeyword (self._column, keyword, value, makesubrecord);

    def putkeywords (self, value):
        """Put the value of multiple table keywords.
        (see :func:`table.putcolkeywords`)"""
        return self._table.putcolkeywords (self._column, value);

    def removekeyword (self, keyword):
        """Remove a column keyword.
        (see :func:`table.removecolkeyword`)"""
        return self._table.removecolkeyword (self._column, keyword);

    def getdesc (self):
        """Get the description of the column.
        (see :func:`table.getcoldesc`)"""
        return self._table.getcoldesc (self._column);

    def getdminfo (self):
        """Get data manager info of the column.
        (see :func:`table.getdminfo`)"""
        return self._table.getdminfo (self._column);

    def iter (self, order='', sort=True):
        """Return a :class:`tableiter` object on this column."""
        from tables import tableiter;
        return tableiter (self._table, [self._column], order, sort);

    def index (self, sort=True):
        """Return a :class:`tableindex` object on this column."""
        from tables import tableindex;
        return tableindex (self._table, [self._column], sort);

    def __len__ (self):
        return self._table.nrows();

    def __getitem__ (self, key):
        sei = self.checkkey (key, self._table.nrows());
        if len(sei) == 1:
            # A single row.
            return self.getcell (sei[0]);
        # Handle row by row and store values in a list.
        result = [];
        rownr  = sei[0];
        inx    = 0;
        while inx < sei[1]:
            result.append (self.getcell (rownr));
            rownr += sei[2];
            inx   += 1;
        return result;

    def __setitem__ (self, key, value):
        sei = self.checkkey (key, self._table.nrows());
        if len(sei) == 1:
            # A single row.
            return self.putcell (sei[0], value);
        # Handle row by row.
        rownr = sei[0];
        inx   = 0;
        if not (isinstance(value,list) or isinstance(value,tuple)):
            # The same value is put in all rows.
            while inx < sei[1]:
                self.putcell (rownr, value);
                rownr += sei[2];
                inx   += 1;
        else:
            # Each row has its own value.
            if len(value) != sei[1]:
                raise RuntimeError("tablecolumn slice length differs from value length")
            for val in value:
                self.putcell (rownr, val);
                rownr += sei[2];
        return True;
        
    def checkkey (self, key, nrows):
        if not isinstance(key, slice):
            # A single index (possibly negative, thus from the end).
            if key < 0:
                key += nrows;
            if key < 0  or  key >= nrows:
                raise IndexError("tablecolumn index out of range");
            return [key];
        # Given as start:stop:step where each part is optional and can
        # be negative.
        incr = 1;
        if key.step != None:
            incr = key.step;
            if incr == 0:
                raise RunTimeError("tablecolumn slice step cannot be zero");
        strow  = 0;
        endrow = nrows;
        if incr < 0:
            strow  = nrows-1;
            endrow = -1;
        if key.start != None:
            strow = key.start;
            if strow < 0:
                strow += nrows;
            strow = min(max(strow,0), nrows-1);
        if key.stop != None:
            endrow = key.stop;
            if endrow < 0:
                endrow += nrows;
            endrow = min(max(endrow,-1), nrows);
        if incr > 0:
            nrow = int((endrow - strow + incr - 1) / incr);
        else:
            nrow = int((strow - endrow - incr - 1) / -incr);
        nrow = max(0, nrow);
        return [strow,nrow,incr];
