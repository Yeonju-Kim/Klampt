# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.11
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.




"""
Python interface to KrisLibrary motion planing routines
"""


from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_motionplanning', [dirname(__file__)])
        except ImportError:
            import _motionplanning
            return _motionplanning
        if fp is not None:
            try:
                _mod = imp.load_module('_motionplanning', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _motionplanning = swig_import_helper()
    del swig_import_helper
else:
    import _motionplanning
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0



def setRandomSeed(*args):
  """
    setRandomSeed(int seed)

    void setRandomSeed(int seed)

    Sets the random seed used by the motion planner. 
    """
  return _motionplanning.setRandomSeed(*args)

def setPlanJSONString(*args):
  """
    setPlanJSONString(char const * string)

    void
    setPlanJSONString(const char *string)

    Loads planner values from a JSON string. 
    """
  return _motionplanning.setPlanJSONString(*args)

def getPlanJSONString():
  """
    getPlanJSONString() -> std::string

    std::string
    getPlanJSONString()

    Saves planner values to a JSON string. 
    """
  return _motionplanning.getPlanJSONString()

def setPlanType(*args):
  """
    setPlanType(char const * type)

    void setPlanType(const char
    *type)

    Sets the planner type.

    Valid values are prm: the Probabilistic Roadmap algorithm

    rrt: the Rapidly Exploring Random Trees algorithm

    sbl: the Single-Query Bidirectional Lazy planner

    sblprt: the probabilistic roadmap of trees (PRT) algorithm with SBL as
    the inter-root planner.

    rrt*: the RRT* algorithm for optimal motion planning

    prm*: the PRM* algorithm for optimal motion planning

    lazyprm*: the Lazy-PRM* algorithm for optimal motion planning

    lazyrrg*: the Lazy-RRG* algorithm for optimal motion planning

    fmm: the fast marching method algorithm for resolution-complete
    optimal motion planning

    fmm*: an anytime fast marching method algorithm for optimal motion
    planning 
    """
  return _motionplanning.setPlanType(*args)

def setPlanSetting(*args):
  """
    setPlanSetting(char const * setting, double value)
    setPlanSetting(char const * setting, char const * value)

    void setPlanSetting(const char
    *setting, const char *value)

    Sets a numeric or string-valued setting for the planner.

    Valid numeric values are: "knn": k value for the k-nearest neighbor
    connection strategy (only for PRM)

    "connectionThreshold": a milestone connection threshold

    "perturbationRadius": (for RRT and SBL)

    "bidirectional": 1 if bidirectional planning is requested (for RRT)

    "grid": 1 if a point selection grid should be used (for SBL)

    "gridResolution": resolution for the grid, if the grid should be
    used (for SBL with grid, FMM, FMM*)

    "suboptimalityFactor": allowable suboptimality (for RRT*, lazy PRM*,
    lazy RRG*)

    "randomizeFrequency": a grid randomization frequency (for SBL)

    "shortcut": nonzero if you wish to perform shortcutting after a
    first plan is found.

    "restart": nonzero if you wish to restart the planner to get better
    paths with the remaining time.

    Valid string values are: "pointLocation": a string designating a
    point location data structure. "kdtree" is supported, optionally
    followed by a weight vector (for PRM, RRT*, PRM*, LazyPRM*, LazyRRG*)

    "restartTermCond": used if the "restart" setting is true. This is
    a JSON string defining the termination condition (default value:
    "{foundSolution:1;maxIters:1000}") 
    """
  return _motionplanning.setPlanSetting(*args)

def destroy():
  """
    destroy()

    void destroy()

    destroys internal data structures 
    """
  return _motionplanning.destroy()
class CSpaceInterface(_object):
    """
    A raw interface for a configuration space. Note: the native Python
    CSpace interface class in cspace.py is easier to use.

    You can either set a single feasibility test function using
    setFeasibility() or add several feasibility tests, all of which need
    to be satisfied, using addFeasibilityTest(). In the latter case,
    planners may be able to provide debugging statistics, solve Minimum
    Constraint Removal problems, run faster by eliminating constraint
    tests, etc.

    Either setVisibility() or setVisibilityEpsilon() must be called to
    define a visibility checker between two (feasible) configurations. In
    the latter case, the path will be discretized at the resolution sent
    to setVisibilityEpsilon. If you have special single-constraint
    visibility tests, you can call that using addVisibilityTest (for
    example, for convex constraints you can set it to the lambda function
    that returns true regardless of its arguments).

    Supported properties include "euclidean" (boolean), "metric"
    (string), "geodesic" (boolean). These may be used by planners to
    make planning faster or more accurate. For a more complete list see
    KrisLibrary/planning/CSpace.h.

    C++ includes: motionplanning.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, CSpaceInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, CSpaceInterface, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(CSpaceInterface self) -> CSpaceInterface
        __init__(CSpaceInterface self, CSpaceInterface arg2) -> CSpaceInterface

        CSpaceInterface::CSpaceInterface(const CSpaceInterface &) 
        """
        this = _motionplanning.new_CSpaceInterface(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _motionplanning.delete_CSpaceInterface
    __del__ = lambda self : None;
    def destroy(self):
        """
        destroy(CSpaceInterface self)

        void
        CSpaceInterface::destroy() 
        """
        return _motionplanning.CSpaceInterface_destroy(self)

    def setFeasibility(self, *args):
        """
        setFeasibility(CSpaceInterface self, PyObject * pyFeas)

        void
        CSpaceInterface::setFeasibility(PyObject *pyFeas) 
        """
        return _motionplanning.CSpaceInterface_setFeasibility(self, *args)

    def addFeasibilityTest(self, *args):
        """
        addFeasibilityTest(CSpaceInterface self, char const * name, PyObject * pyFeas)

        void
        CSpaceInterface::addFeasibilityTest(const char *name, PyObject
        *pyFeas) 
        """
        return _motionplanning.CSpaceInterface_addFeasibilityTest(self, *args)

    def setVisibility(self, *args):
        """
        setVisibility(CSpaceInterface self, PyObject * pyVisible)

        void
        CSpaceInterface::setVisibility(PyObject *pyVisible) 
        """
        return _motionplanning.CSpaceInterface_setVisibility(self, *args)

    def addVisibilityTest(self, *args):
        """
        addVisibilityTest(CSpaceInterface self, char const * name, PyObject * pyVisible)

        void
        CSpaceInterface::addVisibilityTest(const char *name, PyObject
        *pyVisible) 
        """
        return _motionplanning.CSpaceInterface_addVisibilityTest(self, *args)

    def setVisibilityEpsilon(self, *args):
        """
        setVisibilityEpsilon(CSpaceInterface self, double eps)

        void
        CSpaceInterface::setVisibilityEpsilon(double eps) 
        """
        return _motionplanning.CSpaceInterface_setVisibilityEpsilon(self, *args)

    def setSampler(self, *args):
        """
        setSampler(CSpaceInterface self, PyObject * pySamp)

        void
        CSpaceInterface::setSampler(PyObject *pySamp) 
        """
        return _motionplanning.CSpaceInterface_setSampler(self, *args)

    def setNeighborhoodSampler(self, *args):
        """
        setNeighborhoodSampler(CSpaceInterface self, PyObject * pySamp)

        void
        CSpaceInterface::setNeighborhoodSampler(PyObject *pySamp) 
        """
        return _motionplanning.CSpaceInterface_setNeighborhoodSampler(self, *args)

    def setDistance(self, *args):
        """
        setDistance(CSpaceInterface self, PyObject * pyDist)

        void
        CSpaceInterface::setDistance(PyObject *pyDist) 
        """
        return _motionplanning.CSpaceInterface_setDistance(self, *args)

    def setInterpolate(self, *args):
        """
        setInterpolate(CSpaceInterface self, PyObject * pyInterp)

        void
        CSpaceInterface::setInterpolate(PyObject *pyInterp) 
        """
        return _motionplanning.CSpaceInterface_setInterpolate(self, *args)

    def setProperty(self, *args):
        """
        setProperty(CSpaceInterface self, char const * key, char const * value)

        void
        CSpaceInterface::setProperty(const char *key, const char *value) 
        """
        return _motionplanning.CSpaceInterface_setProperty(self, *args)

    __swig_setmethods__["index"] = _motionplanning.CSpaceInterface_index_set
    __swig_getmethods__["index"] = _motionplanning.CSpaceInterface_index_get
    if _newclass:index = _swig_property(_motionplanning.CSpaceInterface_index_get, _motionplanning.CSpaceInterface_index_set)
CSpaceInterface_swigregister = _motionplanning.CSpaceInterface_swigregister
CSpaceInterface_swigregister(CSpaceInterface)

class PlannerInterface(_object):
    """
    An interface for a motion planner. The MotionPlanner interface in
    cspace.py is somewhat easier to use.

    On construction, uses the planner type specified by setPlanType and
    the settings currently specified by calls to setPlanSetting.

    Point-to-point planning is enabled using the setEndpoints method. This
    is mandatory for RRT and SBL planners. The start and end milestones
    are given by indices 0 and 1, respectively

    PRM can be used in either point-to-point or multi-query mode. In
    multi-query mode, you may call addMilestone(q) to add a new milestone.
    addMilestone() returns the index of that milestone, which can be used
    in later calls to getPath().

    To plan, call planMore(iters) until getPath(0,1) returns non-NULL. The
    return value is a list of configurations.

    To get a roadmap (V,E), call getRoadmap(). V is a list of
    configurations (each configuration is a Python list) and E is a list
    of edges (each edge is a pair (i,j) indexing into V).

    To dump the roadmap to disk, call dump(fn). This saves to a Trivial
    Graph Format (TGF) format.

    C++ includes: motionplanning.h 
    """
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, PlannerInterface, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, PlannerInterface, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        """
        __init__(PlannerInterface self, CSpaceInterface cspace) -> PlannerInterface

        PlannerInterface::PlannerInterface(const CSpaceInterface &cspace) 
        """
        this = _motionplanning.new_PlannerInterface(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _motionplanning.delete_PlannerInterface
    __del__ = lambda self : None;
    def destroy(self):
        """
        destroy(PlannerInterface self)

        void
        PlannerInterface::destroy() 
        """
        return _motionplanning.PlannerInterface_destroy(self)

    def setEndpoints(self, *args):
        """
        setEndpoints(PlannerInterface self, PyObject * start, PyObject * goal) -> bool

        bool
        PlannerInterface::setEndpoints(PyObject *start, PyObject *goal) 
        """
        return _motionplanning.PlannerInterface_setEndpoints(self, *args)

    def addMilestone(self, *args):
        """
        addMilestone(PlannerInterface self, PyObject * milestone) -> int

        int
        PlannerInterface::addMilestone(PyObject *milestone) 
        """
        return _motionplanning.PlannerInterface_addMilestone(self, *args)

    def planMore(self, *args):
        """
        planMore(PlannerInterface self, int iterations)

        void
        PlannerInterface::planMore(int iterations) 
        """
        return _motionplanning.PlannerInterface_planMore(self, *args)

    def getPathEndpoints(self):
        """
        getPathEndpoints(PlannerInterface self) -> PyObject *

        PyObject *
        PlannerInterface::getPathEndpoints() 
        """
        return _motionplanning.PlannerInterface_getPathEndpoints(self)

    def getPath(self, *args):
        """
        getPath(PlannerInterface self, int milestone1, int milestone2) -> PyObject *

        PyObject *
        PlannerInterface::getPath(int milestone1, int milestone2) 
        """
        return _motionplanning.PlannerInterface_getPath(self, *args)

    def getData(self, *args):
        """
        getData(PlannerInterface self, char const * setting) -> double

        double
        PlannerInterface::getData(const char *setting) 
        """
        return _motionplanning.PlannerInterface_getData(self, *args)

    def getStats(self):
        """
        getStats(PlannerInterface self) -> PyObject *

        PyObject *
        PlannerInterface::getStats() 
        """
        return _motionplanning.PlannerInterface_getStats(self)

    def getRoadmap(self):
        """
        getRoadmap(PlannerInterface self) -> PyObject *

        PyObject *
        PlannerInterface::getRoadmap() 
        """
        return _motionplanning.PlannerInterface_getRoadmap(self)

    def dump(self, *args):
        """
        dump(PlannerInterface self, char const * fn)

        void
        PlannerInterface::dump(const char *fn) 
        """
        return _motionplanning.PlannerInterface_dump(self, *args)

    __swig_setmethods__["index"] = _motionplanning.PlannerInterface_index_set
    __swig_getmethods__["index"] = _motionplanning.PlannerInterface_index_get
    if _newclass:index = _swig_property(_motionplanning.PlannerInterface_index_get, _motionplanning.PlannerInterface_index_set)
PlannerInterface_swigregister = _motionplanning.PlannerInterface_swigregister
PlannerInterface_swigregister(PlannerInterface)

# This file is compatible with both classic and new-style classes.


