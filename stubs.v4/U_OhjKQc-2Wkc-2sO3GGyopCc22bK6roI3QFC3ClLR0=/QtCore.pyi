import builtins as _mod_builtins
import sip as _mod_sip

PYQT_CONFIGURATION = _mod_builtins.dict()
PYQT_VERSION = 329986
PYQT_VERSION_STR = '5.9.2'
class QAbstractAnimation(QObject):
    'QAbstractAnimation(parent: QObject = None)'
    Backward = Direction()
    DeleteWhenStopped = DeletionPolicy()
    DeletionPolicy = DeletionPolicy
    Direction = Direction
    Forward = Direction()
    KeepWhenStopped = DeletionPolicy()
    Paused = State()
    Running = State()
    State = State
    Stopped = State()
    __class__ = QAbstractAnimation
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractAnimation(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    def currentLoopChanged(self, int):
        'currentLoopChanged(self, int) [signal]'
        pass
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    def directionChanged(self, QAbstractAnimationDirection):
        'directionChanged(self, QAbstractAnimation.Direction) [signal]'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    def finished(self):
        'finished(self) [signal]'
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    def stateChanged(self, QAbstractAnimationState, QAbstractAnimationState_):
        'stateChanged(self, QAbstractAnimation.State, QAbstractAnimation.State) [signal]'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls, self, int):
        'updateCurrentTime(self, int)'
        pass
    
    @classmethod
    def updateDirection(cls, self, QAbstractAnimationDirection):
        'updateDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def updateState(cls, self, QAbstractAnimationState, QAbstractAnimationState_):
        'updateState(self, QAbstractAnimation.State, QAbstractAnimation.State)'
        pass
    

class QAbstractEventDispatcher(QObject):
    'QAbstractEventDispatcher(parent: QObject = None)'
    TimerInfo = TimerInfo
    __class__ = QAbstractEventDispatcher
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractEventDispatcher(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def aboutToBlock(self):
        'aboutToBlock(self) [signal]'
        pass
    
    def awake(self):
        'awake(self) [signal]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def closingDown(cls, self):
        'closingDown(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def filterNativeEvent(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, sipvoidptr=None):
        'filterNativeEvent(self, Union[QByteArray, bytes, bytearray], sip.voidptr) -> Tuple[bool, int]'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls, self):
        'flush(self)'
        pass
    
    @classmethod
    def hasPendingEvents(cls, self):
        'hasPendingEvents(self) -> bool'
        return True
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def installNativeEventFilter(cls, self, QAbstractNativeEventFilter):
        'installNativeEventFilter(self, QAbstractNativeEventFilter)'
        pass
    
    @classmethod
    def instance(cls, thread: QThread=None):
        'instance(thread: QThread = None) -> QAbstractEventDispatcher'
        pass
    
    @classmethod
    def interrupt(cls, self):
        'interrupt(self)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def processEvents(cls, self, UnionQEventLoopProcessEventsFlags=None, QEventLoopProcessEventsFlag=None):
        'processEvents(self, Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag]) -> bool'
        return True
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def registerEventNotifier(cls, self, QWinEventNotifier):
        'registerEventNotifier(self, QWinEventNotifier) -> bool'
        return True
    
    @classmethod
    def registerSocketNotifier(cls, self, QSocketNotifier):
        'registerSocketNotifier(self, QSocketNotifier)'
        pass
    
    @classmethod
    def registerTimer(cls, self, int, int_, QtTimerType, QObject):
        'registerTimer(self, int, Qt.TimerType, QObject) -> int\nregisterTimer(self, int, int, Qt.TimerType, QObject)'
        return 1
    
    @classmethod
    def registeredTimers(cls, self, QObject):
        'registeredTimers(self, QObject) -> object'
        pass
    
    @classmethod
    def remainingTime(cls, self, int):
        'remainingTime(self, int) -> int'
        return 1
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeNativeEventFilter(cls, self, QAbstractNativeEventFilter):
        'removeNativeEventFilter(self, QAbstractNativeEventFilter)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startingUp(cls, self):
        'startingUp(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def unregisterEventNotifier(cls, self, QWinEventNotifier):
        'unregisterEventNotifier(self, QWinEventNotifier)'
        pass
    
    @classmethod
    def unregisterSocketNotifier(cls, self, QSocketNotifier):
        'unregisterSocketNotifier(self, QSocketNotifier)'
        pass
    
    @classmethod
    def unregisterTimer(cls, self, int):
        'unregisterTimer(self, int) -> bool'
        return True
    
    @classmethod
    def unregisterTimers(cls, self, QObject):
        'unregisterTimers(self, QObject) -> bool'
        return True
    
    @classmethod
    def wakeUp(cls, self):
        'wakeUp(self)'
        pass
    

class QAbstractItemModel(QObject):
    'QAbstractItemModel(parent: QObject = None)'
    HorizontalSortHint = LayoutChangeHint()
    LayoutChangeHint = LayoutChangeHint
    NoLayoutChangeHint = LayoutChangeHint()
    VerticalSortHint = LayoutChangeHint()
    __class__ = QAbstractItemModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractItemModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls, self, QModelIndex, int, int_):
        'beginInsertColumns(self, QModelIndex, int, int)'
        pass
    
    @classmethod
    def beginInsertRows(cls, self, QModelIndex, int, int_):
        'beginInsertRows(self, QModelIndex, int, int)'
        pass
    
    @classmethod
    def beginMoveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'beginMoveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def beginMoveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'beginMoveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def beginRemoveColumns(cls, self, QModelIndex, int, int_):
        'beginRemoveColumns(self, QModelIndex, int, int)'
        pass
    
    @classmethod
    def beginRemoveRows(cls, self, QModelIndex, int, int_):
        'beginRemoveRows(self, QModelIndex, int, int)'
        pass
    
    @classmethod
    def beginResetModel(cls, self):
        'beginResetModel(self)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls, self, QModelIndex, QModelIndex_):
        'changePersistentIndex(self, QModelIndex, QModelIndex)'
        pass
    
    @classmethod
    def changePersistentIndexList(cls, self, object, object_):
        'changePersistentIndexList(self, object, object)'
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls, self, parent: QModelIndex=QModelIndex()):
        'columnCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    def columnsAboutToBeInserted(self, QModelIndex, int, int_):
        'columnsAboutToBeInserted(self, QModelIndex, int, int) [signal]'
        pass
    
    def columnsAboutToBeMoved(self, QModelIndex, int, int_, QModelIndex_, int_1):
        'columnsAboutToBeMoved(self, QModelIndex, int, int, QModelIndex, int) [signal]'
        pass
    
    def columnsAboutToBeRemoved(self, QModelIndex, int, int_):
        'columnsAboutToBeRemoved(self, QModelIndex, int, int) [signal]'
        pass
    
    def columnsInserted(self, QModelIndex, int, int_):
        'columnsInserted(self, QModelIndex, int, int) [signal]'
        pass
    
    def columnsMoved(self, QModelIndex, int, int_, QModelIndex_, int_1):
        'columnsMoved(self, QModelIndex, int, int, QModelIndex, int) [signal]'
        pass
    
    def columnsRemoved(self, QModelIndex, int, int_):
        'columnsRemoved(self, QModelIndex, int, int) [signal]'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls, self, int, int_, object: object=0):
        'createIndex(self, int, int, object: object = 0) -> QModelIndex'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    def dataChanged(self, QModelIndex, QModelIndex_, Iterableint=[]):
        'dataChanged(self, QModelIndex, QModelIndex, Iterable[int] = []) [signal]'
        pass
    
    @classmethod
    def decodeData(cls, self, int, int_, QModelIndex, QDataStream):
        'decodeData(self, int, int, QModelIndex, QDataStream) -> bool'
        return True
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls, self, object, QDataStream):
        'encodeData(self, object, QDataStream)'
        pass
    
    @classmethod
    def endInsertColumns(cls, self):
        'endInsertColumns(self)'
        pass
    
    @classmethod
    def endInsertRows(cls, self):
        'endInsertRows(self)'
        pass
    
    @classmethod
    def endMoveColumns(cls, self):
        'endMoveColumns(self)'
        pass
    
    @classmethod
    def endMoveRows(cls, self):
        'endMoveRows(self)'
        pass
    
    @classmethod
    def endRemoveColumns(cls, self):
        'endRemoveColumns(self)'
        pass
    
    @classmethod
    def endRemoveRows(cls, self):
        'endRemoveRows(self)'
        pass
    
    @classmethod
    def endResetModel(cls, self):
        'endResetModel(self)'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls, self, parent: QModelIndex=QModelIndex()):
        'hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    def layoutAboutToBeChanged(self, object, QAbstractItemModelLayoutChangeHint=QAbstractItemModel.NoLayoutChangeHint):
        'layoutAboutToBeChanged(self, object = QList&lt;QPersistentModelIndex&gt;(), QAbstractItemModel.LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) [signal]'
        pass
    
    def layoutChanged(self, IterableQPersistentModelIndex=[], QAbstractItemModelLayoutChangeHint=QAbstractItemModel.NoLayoutChangeHint):
        'layoutChanged(self, Iterable[QPersistentModelIndex] = [], QAbstractItemModel.LayoutChangeHint = QAbstractItemModel.NoLayoutChangeHint) [signal]'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    def modelAboutToBeReset(self):
        'modelAboutToBeReset(self) [signal]'
        pass
    
    def modelReset(self):
        'modelReset(self) [signal]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self, QModelIndex):
        'parent(self, QModelIndex) -> QModelIndex\nparent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls, self):
        'persistentIndexList(self) -> object'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls, self):
        'resetInternalData(self)'
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    def rowsAboutToBeInserted(self, QModelIndex, int, int_):
        'rowsAboutToBeInserted(self, QModelIndex, int, int) [signal]'
        pass
    
    def rowsAboutToBeMoved(self, QModelIndex, int, int_, QModelIndex_, int_1):
        'rowsAboutToBeMoved(self, QModelIndex, int, int, QModelIndex, int) [signal]'
        pass
    
    def rowsAboutToBeRemoved(self, QModelIndex, int, int_):
        'rowsAboutToBeRemoved(self, QModelIndex, int, int) [signal]'
        pass
    
    def rowsInserted(self, QModelIndex, int, int_):
        'rowsInserted(self, QModelIndex, int, int) [signal]'
        pass
    
    def rowsMoved(self, QModelIndex, int, int_, QModelIndex_, int_1):
        'rowsMoved(self, QModelIndex, int, int, QModelIndex, int) [signal]'
        pass
    
    def rowsRemoved(self, QModelIndex, int, int_):
        'rowsRemoved(self, QModelIndex, int, int) [signal]'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QAbstractListModel(QAbstractItemModel):
    'QAbstractListModel(parent: QObject = None)'
    __class__ = QAbstractListModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractListModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls):
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls):
        pass
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, column: int=0, parent: QModelIndex=QModelIndex()):
        'index(self, int, column: int = 0, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls):
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QAbstractNativeEventFilter(_mod_sip.simplewrapper):
    'QAbstractNativeEventFilter()'
    __class__ = QAbstractNativeEventFilter
    __dict__ = {}
    def __init__(self):
        'QAbstractNativeEventFilter()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def nativeEventFilter(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, sipvoidptr=None):
        'nativeEventFilter(self, Union[QByteArray, bytes, bytearray], sip.voidptr) -> Tuple[bool, int]'
        pass
    

class QAbstractProxyModel(QAbstractItemModel):
    'QAbstractProxyModel(parent: QObject = None)'
    __class__ = QAbstractProxyModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractProxyModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls, self, parent: QModelIndex=QModelIndex()):
        'columnCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls, self, parent: QModelIndex=QModelIndex()):
        'hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> Dict[int, Any]'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def mapFromSource(cls, self, QModelIndex):
        'mapFromSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def mapSelectionFromSource(cls, self, QItemSelection):
        'mapSelectionFromSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapSelectionToSource(cls, self, QItemSelection):
        'mapSelectionToSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapToSource(cls, self, QModelIndex):
        'mapToSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self, QModelIndex):
        'parent(self, QModelIndex) -> QModelIndex\nparent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls, self):
        'resetInternalData(self)'
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setSourceModel(cls, self, QAbstractItemModel):
        'setSourceModel(self, QAbstractItemModel)'
        pass
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def sourceModel(cls, self):
        'sourceModel(self) -> QAbstractItemModel'
        pass
    
    def sourceModelChanged(self):
        'sourceModelChanged(self) [signal]'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QAbstractState(QObject):
    'QAbstractState(parent: QState = None)'
    __class__ = QAbstractState
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QState=None):
        'QAbstractState(parent: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def active(cls, self):
        'active(self) -> bool'
        return True
    
    def activeChanged(self, bool):
        'activeChanged(self, bool) [signal]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    def entered(self):
        'entered(self) [signal]'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    def exited(self):
        'exited(self) [signal]'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onEntry(cls, self, QEvent):
        'onEntry(self, QEvent)'
        pass
    
    @classmethod
    def onExit(cls, self, QEvent):
        'onExit(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentState(cls, self):
        'parentState(self) -> QState'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QAbstractTableModel(QAbstractItemModel):
    'QAbstractTableModel(parent: QObject = None)'
    __class__ = QAbstractTableModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAbstractTableModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls, self, parent: QModelIndex=QModelIndex()):
        'columnCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls):
        pass
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls):
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QAbstractTransition(QObject):
    'QAbstractTransition(sourceState: QState = None)'
    ExternalTransition = TransitionType()
    InternalTransition = TransitionType()
    TransitionType = TransitionType
    __class__ = QAbstractTransition
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, sourceState: QState=None):
        'QAbstractTransition(sourceState: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def animations(cls, self):
        'animations(self) -> object'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def eventTest(cls, self, QEvent):
        'eventTest(self, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onTransition(cls, self, QEvent):
        'onTransition(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTargetState(cls, self, QAbstractState):
        'setTargetState(self, QAbstractState)'
        pass
    
    @classmethod
    def setTargetStates(cls, self, IterableQAbstractState=None):
        'setTargetStates(self, Iterable[QAbstractState])'
        pass
    
    @classmethod
    def setTransitionType(cls, self, QAbstractTransitionTransitionType):
        'setTransitionType(self, QAbstractTransition.TransitionType)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sourceState(cls, self):
        'sourceState(self) -> QState'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def targetState(cls, self):
        'targetState(self) -> QAbstractState'
        pass
    
    def targetStateChanged(self):
        'targetStateChanged(self) [signal]'
        pass
    
    @classmethod
    def targetStates(cls, self):
        'targetStates(self) -> object'
        pass
    
    def targetStatesChanged(self):
        'targetStatesChanged(self) [signal]'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transitionType(cls, self):
        'transitionType(self) -> QAbstractTransition.TransitionType'
        pass
    
    def triggered(self):
        'triggered(self) [signal]'
        pass
    

class QAnimationGroup(QAbstractAnimation):
    'QAnimationGroup(parent: QObject = None)'
    __class__ = QAnimationGroup
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QAnimationGroup(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def animationAt(cls, self, int):
        'animationAt(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def animationCount(cls, self):
        'animationCount(self) -> int'
        return 1
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def indexOfAnimation(cls, self, QAbstractAnimation):
        'indexOfAnimation(self, QAbstractAnimation) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertAnimation(cls, self, int, QAbstractAnimation):
        'insertAnimation(self, int, QAbstractAnimation)'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def takeAnimation(cls, self, int):
        'takeAnimation(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls):
        pass
    
    @classmethod
    def updateDirection(cls):
        pass
    
    @classmethod
    def updateState(cls):
        pass
    

class QBasicTimer(_mod_sip.simplewrapper):
    'QBasicTimer()\nQBasicTimer(QBasicTimer)'
    __class__ = QBasicTimer
    __dict__ = {}
    def __init__(self, QBasicTimer):
        'QBasicTimer()\nQBasicTimer(QBasicTimer)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def isActive(cls, self):
        'isActive(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, int, QtTimerType, QObject):
        'start(self, int, Qt.TimerType, QObject)\nstart(self, int, QObject)'
        pass
    
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def timerId(cls, self):
        'timerId(self) -> int'
        return 1
    

class QBitArray(_mod_sip.simplewrapper):
    'QBitArray()\nQBitArray(int, value: bool = False)\nQBitArray(QBitArray)'
    def __and__(self, value):
        'Return self&value.'
        return QBitArray()
    
    __class__ = QBitArray
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __iand__(self, value):
        'Return self&=value.'
        return None
    
    def __init__(self, int, value: bool=False):
        'QBitArray()\nQBitArray(int, value: bool = False)\nQBitArray(QBitArray)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __invert__(self):
        '~self'
        return QBitArray()
    
    def __ior__(self, value):
        'Return self|=value.'
        return None
    
    def __ixor__(self, value):
        'Return self^=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __or__(self, value):
        'Return self|value.'
        return QBitArray()
    
    def __rand__(self, value):
        'Return value&self.'
        return QBitArray()
    
    def __ror__(self, value):
        'Return value|self.'
        return QBitArray()
    
    def __rxor__(self, value):
        'Return value^self.'
        return QBitArray()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    def __xor__(self, value):
        'Return self^value.'
        return QBitArray()
    
    @classmethod
    def at(cls, self, int):
        'at(self, int) -> bool'
        return True
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def clearBit(cls, self, int):
        'clearBit(self, int)'
        pass
    
    @classmethod
    def count(cls, self, bool):
        'count(self) -> int\ncount(self, bool) -> int'
        return 1
    
    @classmethod
    def detach(cls, self):
        'detach(self)'
        pass
    
    @classmethod
    def fill(cls, self, bool, size: int=-1):
        'fill(self, bool, int, int)\nfill(self, bool, size: int = -1) -> bool'
        pass
    
    @classmethod
    def isDetached(cls, self):
        'isDetached(self) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int)'
        pass
    
    @classmethod
    def setBit(cls, self, int, bool):
        'setBit(self, int)\nsetBit(self, int, bool)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def swap(cls, self, QBitArray):
        'swap(self, QBitArray)'
        pass
    
    @classmethod
    def testBit(cls, self, int):
        'testBit(self, int) -> bool'
        return True
    
    @classmethod
    def toggleBit(cls, self, int):
        'toggleBit(self, int) -> bool'
        return True
    
    @classmethod
    def truncate(cls, self, int):
        'truncate(self, int)'
        pass
    

class QBuffer(QIODevice):
    'QBuffer(parent: QObject = None)\nQBuffer(QByteArray, parent: QObject = None)'
    __class__ = QBuffer
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QByteArray, parent: QObject=None):
        'QBuffer(parent: QObject = None)\nQBuffer(QByteArray, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buffer(cls, self):
        'buffer(self) -> QByteArray'
        pass
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls, self, QMetaMethod):
        'connectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self):
        'data(self) -> QByteArray'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls, self, QMetaMethod):
        'disconnectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls, self, int):
        'readData(self, int) -> bytes'
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls):
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setBuffer(cls, self, QByteArray):
        'setBuffer(self, QByteArray)'
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setData(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'setData(self, Union[QByteArray, bytes, bytearray])\nsetData(self, bytes)'
        pass
    
    @classmethod
    def setErrorString(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls):
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls, self, bytes):
        'writeData(self, bytes) -> int'
        return 1
    

class QByteArray(_mod_sip.simplewrapper):
    'QByteArray()\nQByteArray(int, str)\nQByteArray(Union[QByteArray, bytes, bytearray])'
    Base64Encoding = Base64Option()
    Base64Option = Base64Option
    Base64Options = Base64Options
    Base64UrlEncoding = Base64Option()
    KeepTrailingEquals = Base64Option()
    OmitTrailingEquals = Base64Option()
    def __add__(self, value):
        'Return self+value.'
        return QByteArray()
    
    __class__ = QByteArray
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __iadd__(self, value):
        'Implement self+=value.'
        return None
    
    def __imul__(self, value):
        'Implement self*=value.'
        return None
    
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None):
        'QByteArray()\nQByteArray(int, str)\nQByteArray(Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QByteArray()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QByteArray()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return QByteArray()
    
    def __str__(self):
        'Return str(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def append(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'append(self, Union[QByteArray, bytes, bytearray]) -> QByteArray\nappend(self, str) -> QByteArray\nappend(self, int, str) -> QByteArray'
        pass
    
    @classmethod
    def at(cls, self, int):
        'at(self, int) -> str'
        return ''
    
    @classmethod
    def capacity(cls, self):
        'capacity(self) -> int'
        return 1
    
    @classmethod
    def chop(cls, self, int):
        'chop(self, int)'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def contains(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'contains(self, Union[QByteArray, bytes, bytearray]) -> bool'
        return True
    
    @classmethod
    def count(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'count(self, Union[QByteArray, bytes, bytearray]) -> int\ncount(self) -> int'
        return 1
    
    @classmethod
    def data(cls, self):
        'data(self) -> bytes'
        pass
    
    @classmethod
    def endsWith(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'endsWith(self, Union[QByteArray, bytes, bytearray]) -> bool'
        return True
    
    @classmethod
    def fill(cls, self, str, size: int=-1):
        'fill(self, str, size: int = -1) -> QByteArray'
        pass
    
    @classmethod
    def fromBase64(cls, UnionQByteArray=None, bytes=None, bytearray=None, UnionQByteArrayBase64Options=None, QByteArrayBase64Option=None):
        'fromBase64(Union[QByteArray, bytes, bytearray]) -> QByteArray\nfromBase64(Union[QByteArray, bytes, bytearray], Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray'
        pass
    
    @classmethod
    def fromHex(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'fromHex(Union[QByteArray, bytes, bytearray]) -> QByteArray'
        pass
    
    @classmethod
    def fromPercentEncoding(cls, UnionQByteArray=None, bytes=None, bytearray=None, percent: str='%'):
        "fromPercentEncoding(Union[QByteArray, bytes, bytearray], percent: str = '%') -> QByteArray"
        pass
    
    @classmethod
    def fromRawData(cls, bytes):
        'fromRawData(bytes) -> QByteArray'
        pass
    
    @classmethod
    def indexOf(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, from_: int=0):
        'indexOf(self, Union[QByteArray, bytes, bytearray], from_: int = 0) -> int\nindexOf(self, str, from_: int = 0) -> int'
        return 1
    
    @classmethod
    def insert(cls, self, int, UnionQByteArray=None, bytes=None, bytearray=None):
        'insert(self, int, Union[QByteArray, bytes, bytearray]) -> QByteArray\ninsert(self, int, str) -> QByteArray\ninsert(self, int, int, str) -> QByteArray'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def lastIndexOf(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, from_: int=-1):
        'lastIndexOf(self, Union[QByteArray, bytes, bytearray], from_: int = -1) -> int\nlastIndexOf(self, str, from_: int = -1) -> int'
        return 1
    
    @classmethod
    def left(cls, self, int):
        'left(self, int) -> QByteArray'
        pass
    
    @classmethod
    def leftJustified(cls, self, int, fill: str=' ', truncate: bool=False):
        "leftJustified(self, int, fill: str = ' ', truncate: bool = False) -> QByteArray"
        pass
    
    @classmethod
    def length(cls, self):
        'length(self) -> int'
        return 1
    
    @classmethod
    def mid(cls, self, int, length: int=-1):
        'mid(self, int, length: int = -1) -> QByteArray'
        pass
    
    @classmethod
    def number(cls, float, format: str='g', precision: int=6):
        "number(int, base: int = 10) -> QByteArray\nnumber(float, format: str = 'g', precision: int = 6) -> QByteArray\nnumber(int, base: int = 10) -> QByteArray\nnumber(int, base: int = 10) -> QByteArray"
        pass
    
    @classmethod
    def prepend(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'prepend(self, Union[QByteArray, bytes, bytearray]) -> QByteArray\nprepend(self, int, str) -> QByteArray'
        pass
    
    @classmethod
    def push_back(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'push_back(self, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def push_front(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'push_front(self, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def remove(cls, self, int, int_):
        'remove(self, int, int) -> QByteArray'
        pass
    
    @classmethod
    def repeated(cls, self, int):
        'repeated(self, int) -> QByteArray'
        pass
    
    @classmethod
    def replace(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, UnionQByteArray_=None, bytes_=None, bytearray_=None):
        'replace(self, int, int, Union[QByteArray, bytes, bytearray]) -> QByteArray\nreplace(self, Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray]) -> QByteArray\nreplace(self, str, Union[QByteArray, bytes, bytearray]) -> QByteArray'
        pass
    
    @classmethod
    def reserve(cls, self, int):
        'reserve(self, int)'
        pass
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int)'
        pass
    
    @classmethod
    def right(cls, self, int):
        'right(self, int) -> QByteArray'
        pass
    
    @classmethod
    def rightJustified(cls, self, int, fill: str=' ', truncate: bool=False):
        "rightJustified(self, int, fill: str = ' ', truncate: bool = False) -> QByteArray"
        pass
    
    @classmethod
    def setNum(cls, self, float, format: str='g', precision: int=6):
        "setNum(self, int, base: int = 10) -> QByteArray\nsetNum(self, float, format: str = 'g', precision: int = 6) -> QByteArray\nsetNum(self, int, base: int = 10) -> QByteArray\nsetNum(self, int, base: int = 10) -> QByteArray"
        pass
    
    @classmethod
    def simplified(cls, self):
        'simplified(self) -> QByteArray'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def split(cls, self, str):
        'split(self, str) -> List[QByteArray]'
        pass
    
    @classmethod
    def squeeze(cls, self):
        'squeeze(self)'
        pass
    
    @classmethod
    def startsWith(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'startsWith(self, Union[QByteArray, bytes, bytearray]) -> bool'
        return True
    
    @classmethod
    def swap(cls, self, QByteArray):
        'swap(self, QByteArray)'
        pass
    
    @classmethod
    def toBase64(cls, self, UnionQByteArrayBase64Options=None, QByteArrayBase64Option=None):
        'toBase64(self) -> QByteArray\ntoBase64(self, Union[QByteArray.Base64Options, QByteArray.Base64Option]) -> QByteArray'
        pass
    
    @classmethod
    def toDouble(cls, self):
        'toDouble(self) -> Tuple[float, bool]'
        pass
    
    @classmethod
    def toFloat(cls, self):
        'toFloat(self) -> Tuple[float, bool]'
        pass
    
    @classmethod
    def toHex(cls, self, str):
        'toHex(self) -> QByteArray\ntoHex(self, str) -> QByteArray'
        pass
    
    @classmethod
    def toInt(cls, self, base: int=10):
        'toInt(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toLong(cls, self, base: int=10):
        'toLong(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toLongLong(cls, self, base: int=10):
        'toLongLong(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toLower(cls, self):
        'toLower(self) -> QByteArray'
        pass
    
    @classmethod
    def toPercentEncoding(cls, self, exclude: Union[QByteArray,bytes,bytearray]=QByteArray(), include: Union[QByteArray,bytes,bytearray]=QByteArray(), percent: str='%'):
        "toPercentEncoding(self, exclude: Union[QByteArray, bytes, bytearray] = QByteArray(), include: Union[QByteArray, bytes, bytearray] = QByteArray(), percent: str = '%') -> QByteArray"
        pass
    
    @classmethod
    def toShort(cls, self, base: int=10):
        'toShort(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toUInt(cls, self, base: int=10):
        'toUInt(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toULong(cls, self, base: int=10):
        'toULong(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toULongLong(cls, self, base: int=10):
        'toULongLong(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toUShort(cls, self, base: int=10):
        'toUShort(self, base: int = 10) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toUpper(cls, self):
        'toUpper(self) -> QByteArray'
        pass
    
    @classmethod
    def trimmed(cls, self):
        'trimmed(self) -> QByteArray'
        pass
    
    @classmethod
    def truncate(cls, self, int):
        'truncate(self, int)'
        pass
    

class QByteArrayMatcher(_mod_sip.simplewrapper):
    'QByteArrayMatcher()\nQByteArrayMatcher(Union[QByteArray, bytes, bytearray])\nQByteArrayMatcher(QByteArrayMatcher)'
    __class__ = QByteArrayMatcher
    __dict__ = {}
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None):
        'QByteArrayMatcher()\nQByteArrayMatcher(Union[QByteArray, bytes, bytearray])\nQByteArrayMatcher(QByteArrayMatcher)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def indexIn(cls, self, UnionQByteArray=None, bytes=None, bytearray=None, from_: int=0):
        'indexIn(self, Union[QByteArray, bytes, bytearray], from_: int = 0) -> int'
        return 1
    
    @classmethod
    def pattern(cls, self):
        'pattern(self) -> QByteArray'
        pass
    
    @classmethod
    def setPattern(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'setPattern(self, Union[QByteArray, bytes, bytearray])'
        pass
    

class QChildEvent(QEvent):
    'QChildEvent(QEvent.Type, QObject)\nQChildEvent(QChildEvent)'
    __class__ = QChildEvent
    __dict__ = {}
    def __init__(self, QEventType, QObject):
        'QChildEvent(QEvent.Type, QObject)\nQChildEvent(QChildEvent)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def accept(cls, self):
        'accept(self)'
        pass
    
    @classmethod
    def added(cls, self):
        'added(self) -> bool'
        return True
    
    @classmethod
    def child(cls, self):
        'child(self) -> QObject'
        pass
    
    @classmethod
    def ignore(cls, self):
        'ignore(self)'
        pass
    
    @classmethod
    def isAccepted(cls, self):
        'isAccepted(self) -> bool'
        return True
    
    @classmethod
    def polished(cls, self):
        'polished(self) -> bool'
        return True
    
    @classmethod
    def registerEventType(cls, hint: int=-1):
        'registerEventType(hint: int = -1) -> int'
        return 1
    
    @classmethod
    def removed(cls, self):
        'removed(self) -> bool'
        return True
    
    @classmethod
    def setAccepted(cls, self, bool):
        'setAccepted(self, bool)'
        pass
    
    @classmethod
    def spontaneous(cls, self):
        'spontaneous(self) -> bool'
        return True
    
    @classmethod
    def type(cls, self):
        'type(self) -> QEvent.Type'
        pass
    

class QCollator(_mod_sip.simplewrapper):
    'QCollator(locale: QLocale = QLocale())\nQCollator(QCollator)'
    __class__ = QCollator
    __dict__ = {}
    def __init__(self, locale: QLocale=QLocale()):
        'QCollator(locale: QLocale = QLocale())\nQCollator(QCollator)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def caseSensitivity(cls, self):
        'caseSensitivity(self) -> Qt.CaseSensitivity'
        pass
    
    @classmethod
    def compare(cls, self, str, str_):
        'compare(self, str, str) -> int'
        return 1
    
    @classmethod
    def ignorePunctuation(cls, self):
        'ignorePunctuation(self) -> bool'
        return True
    
    @classmethod
    def locale(cls, self):
        'locale(self) -> QLocale'
        pass
    
    @classmethod
    def numericMode(cls, self):
        'numericMode(self) -> bool'
        return True
    
    @classmethod
    def setCaseSensitivity(cls, self, QtCaseSensitivity):
        'setCaseSensitivity(self, Qt.CaseSensitivity)'
        pass
    
    @classmethod
    def setIgnorePunctuation(cls, self, bool):
        'setIgnorePunctuation(self, bool)'
        pass
    
    @classmethod
    def setLocale(cls, self, QLocale):
        'setLocale(self, QLocale)'
        pass
    
    @classmethod
    def setNumericMode(cls, self, bool):
        'setNumericMode(self, bool)'
        pass
    
    @classmethod
    def sortKey(cls, self, str):
        'sortKey(self, str) -> QCollatorSortKey'
        pass
    
    @classmethod
    def swap(cls, self, QCollator):
        'swap(self, QCollator)'
        pass
    

class QCollatorSortKey(_mod_sip.simplewrapper):
    'QCollatorSortKey(QCollatorSortKey)'
    __class__ = QCollatorSortKey
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QCollatorSortKey):
        'QCollatorSortKey(QCollatorSortKey)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def compare(cls, self, QCollatorSortKey):
        'compare(self, QCollatorSortKey) -> int'
        return 1
    
    @classmethod
    def swap(cls, self, QCollatorSortKey):
        'swap(self, QCollatorSortKey)'
        pass
    

class QCommandLineOption(_mod_sip.simplewrapper):
    "QCommandLineOption(str)\nQCommandLineOption(Iterable[str])\nQCommandLineOption(str, str, valueName: str = '', defaultValue: str = '')\nQCommandLineOption(Iterable[str], str, valueName: str = '', defaultValue: str = '')\nQCommandLineOption(QCommandLineOption)"
    Flag = Flag
    Flags = Flags
    HiddenFromHelp = Flag()
    ShortOptionStyle = Flag()
    __class__ = QCommandLineOption
    __dict__ = {}
    def __init__(self, Iterablestr=None, str=None, valueName: str='', defaultValue: str=''):
        "QCommandLineOption(str)\nQCommandLineOption(Iterable[str])\nQCommandLineOption(str, str, valueName: str = '', defaultValue: str = '')\nQCommandLineOption(Iterable[str], str, valueName: str = '', defaultValue: str = '')\nQCommandLineOption(QCommandLineOption)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def defaultValues(cls, self):
        'defaultValues(self) -> List[str]'
        pass
    
    @classmethod
    def description(cls, self):
        'description(self) -> str'
        return ''
    
    @classmethod
    def flags(cls, self):
        'flags(self) -> QCommandLineOption.Flags'
        pass
    
    @classmethod
    def isHidden(cls, self):
        'isHidden(self) -> bool'
        return True
    
    @classmethod
    def names(cls, self):
        'names(self) -> List[str]'
        pass
    
    @classmethod
    def setDefaultValue(cls, self, str):
        'setDefaultValue(self, str)'
        pass
    
    @classmethod
    def setDefaultValues(cls, self, Iterablestr=None):
        'setDefaultValues(self, Iterable[str])'
        pass
    
    @classmethod
    def setDescription(cls, self, str):
        'setDescription(self, str)'
        pass
    
    @classmethod
    def setFlags(cls, self, UnionQCommandLineOptionFlags=None, QCommandLineOptionFlag=None):
        'setFlags(self, Union[QCommandLineOption.Flags, QCommandLineOption.Flag])'
        pass
    
    @classmethod
    def setHidden(cls, self, bool):
        'setHidden(self, bool)'
        pass
    
    @classmethod
    def setValueName(cls, self, str):
        'setValueName(self, str)'
        pass
    
    @classmethod
    def swap(cls, self, QCommandLineOption):
        'swap(self, QCommandLineOption)'
        pass
    
    @classmethod
    def valueName(cls, self):
        'valueName(self) -> str'
        return ''
    

class QCommandLineParser(_mod_sip.simplewrapper):
    'QCommandLineParser()'
    OptionsAfterPositionalArgumentsMode = OptionsAfterPositionalArgumentsMode
    ParseAsCompactedShortOptions = SingleDashWordOptionMode()
    ParseAsLongOptions = SingleDashWordOptionMode()
    ParseAsOptions = OptionsAfterPositionalArgumentsMode()
    ParseAsPositionalArguments = OptionsAfterPositionalArgumentsMode()
    SingleDashWordOptionMode = SingleDashWordOptionMode
    __class__ = QCommandLineParser
    __dict__ = {}
    def __init__(self):
        'QCommandLineParser()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addHelpOption(cls, self):
        'addHelpOption(self) -> QCommandLineOption'
        pass
    
    @classmethod
    def addOption(cls, self, QCommandLineOption):
        'addOption(self, QCommandLineOption) -> bool'
        return True
    
    @classmethod
    def addOptions(cls, self, object):
        'addOptions(self, object) -> bool'
        return True
    
    @classmethod
    def addPositionalArgument(cls, self, str, str_, syntax: str=''):
        "addPositionalArgument(self, str, str, syntax: str = '')"
        pass
    
    @classmethod
    def addVersionOption(cls, self):
        'addVersionOption(self) -> QCommandLineOption'
        pass
    
    @classmethod
    def applicationDescription(cls, self):
        'applicationDescription(self) -> str'
        return ''
    
    @classmethod
    def clearPositionalArguments(cls, self):
        'clearPositionalArguments(self)'
        pass
    
    @classmethod
    def errorText(cls, self):
        'errorText(self) -> str'
        return ''
    
    @classmethod
    def helpText(cls, self):
        'helpText(self) -> str'
        return ''
    
    @classmethod
    def isSet(cls, self, QCommandLineOption):
        'isSet(self, str) -> bool\nisSet(self, QCommandLineOption) -> bool'
        return True
    
    @classmethod
    def optionNames(cls, self):
        'optionNames(self) -> List[str]'
        pass
    
    @classmethod
    def parse(cls, self, Iterablestr=None):
        'parse(self, Iterable[str]) -> bool'
        return True
    
    @classmethod
    def positionalArguments(cls, self):
        'positionalArguments(self) -> List[str]'
        pass
    
    @classmethod
    def process(cls, self, QCoreApplication):
        'process(self, Iterable[str])\nprocess(self, QCoreApplication)'
        pass
    
    @classmethod
    def setApplicationDescription(cls, self, str):
        'setApplicationDescription(self, str)'
        pass
    
    @classmethod
    def setOptionsAfterPositionalArgumentsMode(cls, self, QCommandLineParserOptionsAfterPositionalArgumentsMode):
        'setOptionsAfterPositionalArgumentsMode(self, QCommandLineParser.OptionsAfterPositionalArgumentsMode)'
        pass
    
    @classmethod
    def setSingleDashWordOptionMode(cls, self, QCommandLineParserSingleDashWordOptionMode):
        'setSingleDashWordOptionMode(self, QCommandLineParser.SingleDashWordOptionMode)'
        pass
    
    @classmethod
    def showHelp(cls, self, exitCode: int=0):
        'showHelp(self, exitCode: int = 0)'
        pass
    
    @classmethod
    def showVersion(cls, self):
        'showVersion(self)'
        pass
    
    @classmethod
    def unknownOptionNames(cls, self):
        'unknownOptionNames(self) -> List[str]'
        pass
    
    @classmethod
    def value(cls, self, QCommandLineOption):
        'value(self, str) -> str\nvalue(self, QCommandLineOption) -> str'
        return ''
    
    @classmethod
    def values(cls, self, QCommandLineOption):
        'values(self, str) -> List[str]\nvalues(self, QCommandLineOption) -> List[str]'
        pass
    

class QCoreApplication(QObject):
    'QCoreApplication(List[str])'
    __class__ = QCoreApplication
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, Liststr=None):
        'QCoreApplication(List[str])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def aboutToQuit(self):
        'aboutToQuit(self) [signal]'
        pass
    
    @classmethod
    def addLibraryPath(cls, str):
        'addLibraryPath(str)'
        pass
    
    @classmethod
    def applicationDirPath(cls):
        'applicationDirPath() -> str'
        return ''
    
    @classmethod
    def applicationFilePath(cls):
        'applicationFilePath() -> str'
        return ''
    
    @classmethod
    def applicationName(cls):
        'applicationName() -> str'
        return ''
    
    @classmethod
    def applicationPid(cls):
        'applicationPid() -> int'
        return 1
    
    @classmethod
    def applicationVersion(cls):
        'applicationVersion() -> str'
        return ''
    
    @classmethod
    def arguments(cls):
        'arguments() -> List[str]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def closingDown(cls):
        'closingDown() -> bool'
        return True
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventDispatcher(cls):
        'eventDispatcher() -> QAbstractEventDispatcher'
        pass
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def exec(cls):
        'exec() -> int'
        return 1
    
    @classmethod
    def exec_(cls):
        'exec_() -> int'
        return 1
    
    @classmethod
    def exit(cls, returnCode: int=0):
        'exit(returnCode: int = 0)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls):
        'flush()'
        pass
    
    @classmethod
    def hasPendingEvents(cls):
        'hasPendingEvents() -> bool'
        return True
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def installNativeEventFilter(cls, self, QAbstractNativeEventFilter):
        'installNativeEventFilter(self, QAbstractNativeEventFilter)'
        pass
    
    @classmethod
    def installTranslator(cls, QTranslator):
        'installTranslator(QTranslator) -> bool'
        return True
    
    @classmethod
    def instance(cls):
        'instance() -> QCoreApplication'
        pass
    
    @classmethod
    def isQuitLockEnabled(cls):
        'isQuitLockEnabled() -> bool'
        return True
    
    @classmethod
    def isSetuidAllowed(cls):
        'isSetuidAllowed() -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def libraryPaths(cls):
        'libraryPaths() -> List[str]'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def notify(cls, self, QObject, QEvent):
        'notify(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def organizationDomain(cls):
        'organizationDomain() -> str'
        return ''
    
    @classmethod
    def organizationName(cls):
        'organizationName() -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def postEvent(cls, QObject, QEvent, priority: int=Qt.NormalEventPriority):
        'postEvent(QObject, QEvent, priority: int = Qt.NormalEventPriority)'
        pass
    
    @classmethod
    def processEvents(cls, flags: Union[QEventLoop.ProcessEventsFlags,QEventLoop.ProcessEventsFlag]=QEventLoop.AllEvents):
        'processEvents(flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.AllEvents)\nprocessEvents(Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], int)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def quit(cls):
        'quit()'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeLibraryPath(cls, str):
        'removeLibraryPath(str)'
        pass
    
    @classmethod
    def removeNativeEventFilter(cls, self, QAbstractNativeEventFilter):
        'removeNativeEventFilter(self, QAbstractNativeEventFilter)'
        pass
    
    @classmethod
    def removePostedEvents(cls, QObject, eventType: int=0):
        'removePostedEvents(QObject, eventType: int = 0)'
        pass
    
    @classmethod
    def removeTranslator(cls, QTranslator):
        'removeTranslator(QTranslator) -> bool'
        return True
    
    @classmethod
    def sendEvent(cls, QObject, QEvent):
        'sendEvent(QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def sendPostedEvents(cls, receiver: QObject=None, eventType: int=0):
        'sendPostedEvents(receiver: QObject = None, eventType: int = 0)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setApplicationName(cls, str):
        'setApplicationName(str)'
        pass
    
    @classmethod
    def setApplicationVersion(cls, str):
        'setApplicationVersion(str)'
        pass
    
    @classmethod
    def setAttribute(cls, QtApplicationAttribute, on: bool=True):
        'setAttribute(Qt.ApplicationAttribute, on: bool = True)'
        pass
    
    @classmethod
    def setEventDispatcher(cls, QAbstractEventDispatcher):
        'setEventDispatcher(QAbstractEventDispatcher)'
        pass
    
    @classmethod
    def setLibraryPaths(cls, Iterablestr=None):
        'setLibraryPaths(Iterable[str])'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOrganizationDomain(cls, str):
        'setOrganizationDomain(str)'
        pass
    
    @classmethod
    def setOrganizationName(cls, str):
        'setOrganizationName(str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setQuitLockEnabled(cls, bool):
        'setQuitLockEnabled(bool)'
        pass
    
    @classmethod
    def setSetuidAllowed(cls, bool):
        'setSetuidAllowed(bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startingUp(cls):
        'startingUp() -> bool'
        return True
    
    staticMetaObject = QMetaObject()
    @classmethod
    def testAttribute(cls, QtApplicationAttribute):
        'testAttribute(Qt.ApplicationAttribute) -> bool'
        return True
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def translate(cls, str, str_, disambiguation: str=None, n: int=-1):
        'translate(str, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QCryptographicHash(_mod_sip.simplewrapper):
    'QCryptographicHash(QCryptographicHash.Algorithm)'
    Algorithm = Algorithm
    Keccak_224 = Algorithm()
    Keccak_256 = Algorithm()
    Keccak_384 = Algorithm()
    Keccak_512 = Algorithm()
    Md4 = Algorithm()
    Md5 = Algorithm()
    Sha1 = Algorithm()
    Sha224 = Algorithm()
    Sha256 = Algorithm()
    Sha384 = Algorithm()
    Sha3_224 = Algorithm()
    Sha3_256 = Algorithm()
    Sha3_384 = Algorithm()
    Sha3_512 = Algorithm()
    Sha512 = Algorithm()
    __class__ = QCryptographicHash
    __dict__ = {}
    def __init__(self, QCryptographicHashAlgorithm):
        'QCryptographicHash(QCryptographicHash.Algorithm)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addData(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'addData(self, bytes)\naddData(self, Union[QByteArray, bytes, bytearray])\naddData(self, QIODevice) -> bool'
        pass
    
    @classmethod
    def hash(cls, UnionQByteArray=None, bytes=None, bytearray=None, QCryptographicHashAlgorithm=None):
        'hash(Union[QByteArray, bytes, bytearray], QCryptographicHash.Algorithm) -> QByteArray'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self)'
        pass
    
    @classmethod
    def result(cls, self):
        'result(self) -> QByteArray'
        pass
    

class QDataStream(_mod_sip.simplewrapper):
    'QDataStream()\nQDataStream(QIODevice)\nQDataStream(QByteArray, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag])\nQDataStream(QByteArray)'
    BigEndian = ByteOrder()
    ByteOrder = ByteOrder
    DoublePrecision = FloatingPointPrecision()
    FloatingPointPrecision = FloatingPointPrecision
    LittleEndian = ByteOrder()
    Ok = Status()
    Qt_1_0 = Version()
    Qt_2_0 = Version()
    Qt_2_1 = Version()
    Qt_3_0 = Version()
    Qt_3_1 = Version()
    Qt_3_3 = Version()
    Qt_4_0 = Version()
    Qt_4_1 = Version()
    Qt_4_2 = Version()
    Qt_4_3 = Version()
    Qt_4_4 = Version()
    Qt_4_5 = Version()
    Qt_4_6 = Version()
    Qt_4_7 = Version()
    Qt_4_8 = Version()
    Qt_4_9 = Version()
    Qt_5_0 = Version()
    Qt_5_1 = Version()
    Qt_5_2 = Version()
    Qt_5_3 = Version()
    Qt_5_4 = Version()
    Qt_5_5 = Version()
    Qt_5_6 = Version()
    Qt_5_7 = Version()
    Qt_5_8 = Version()
    Qt_5_9 = Version()
    ReadCorruptData = Status()
    ReadPastEnd = Status()
    SinglePrecision = FloatingPointPrecision()
    Status = Status
    Version = Version
    WriteFailed = Status()
    __class__ = QDataStream
    __dict__ = {}
    def __init__(self, QByteArray, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'QDataStream()\nQDataStream(QIODevice)\nQDataStream(QByteArray, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag])\nQDataStream(QByteArray)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lshift__(self, value):
        'Return self<<value.'
        return QDataStream()
    
    __module__ = 'PyQt5.QtCore'
    def __rlshift__(self, value):
        'Return value<<self.'
        return QDataStream()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QDataStream()
    
    def __rshift__(self, value):
        'Return self>>value.'
        return QDataStream()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def abortTransaction(cls, self):
        'abortTransaction(self)'
        pass
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def byteOrder(cls, self):
        'byteOrder(self) -> QDataStream.ByteOrder'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self) -> bool'
        return True
    
    @classmethod
    def device(cls, self):
        'device(self) -> QIODevice'
        pass
    
    @classmethod
    def floatingPointPrecision(cls, self):
        'floatingPointPrecision(self) -> QDataStream.FloatingPointPrecision'
        pass
    
    @classmethod
    def readBool(cls, self):
        'readBool(self) -> bool'
        return True
    
    @classmethod
    def readBytes(cls, self):
        'readBytes(self) -> bytes'
        pass
    
    @classmethod
    def readDouble(cls, self):
        'readDouble(self) -> float'
        return 1.0
    
    @classmethod
    def readFloat(cls, self):
        'readFloat(self) -> float'
        return 1.0
    
    @classmethod
    def readInt(cls, self):
        'readInt(self) -> int'
        return 1
    
    @classmethod
    def readInt16(cls, self):
        'readInt16(self) -> int'
        return 1
    
    @classmethod
    def readInt32(cls, self):
        'readInt32(self) -> int'
        return 1
    
    @classmethod
    def readInt64(cls, self):
        'readInt64(self) -> int'
        return 1
    
    @classmethod
    def readInt8(cls, self):
        'readInt8(self) -> int'
        return 1
    
    @classmethod
    def readQString(cls, self):
        'readQString(self) -> str'
        return ''
    
    @classmethod
    def readQStringList(cls, self):
        'readQStringList(self) -> List[str]'
        pass
    
    @classmethod
    def readQVariant(cls, self):
        'readQVariant(self) -> Any'
        pass
    
    @classmethod
    def readQVariantHash(cls, self):
        'readQVariantHash(self) -> Dict[str, Any]'
        pass
    
    @classmethod
    def readQVariantList(cls, self):
        'readQVariantList(self) -> List[Any]'
        pass
    
    @classmethod
    def readQVariantMap(cls, self):
        'readQVariantMap(self) -> Dict[str, Any]'
        pass
    
    @classmethod
    def readRawData(cls, self, int):
        'readRawData(self, int) -> bytes'
        pass
    
    @classmethod
    def readString(cls, self):
        'readString(self) -> bytes'
        pass
    
    @classmethod
    def readUInt16(cls, self):
        'readUInt16(self) -> int'
        return 1
    
    @classmethod
    def readUInt32(cls, self):
        'readUInt32(self) -> int'
        return 1
    
    @classmethod
    def readUInt64(cls, self):
        'readUInt64(self) -> int'
        return 1
    
    @classmethod
    def readUInt8(cls, self):
        'readUInt8(self) -> int'
        return 1
    
    @classmethod
    def resetStatus(cls, self):
        'resetStatus(self)'
        pass
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def setByteOrder(cls, self, QDataStreamByteOrder):
        'setByteOrder(self, QDataStream.ByteOrder)'
        pass
    
    @classmethod
    def setDevice(cls, self, QIODevice):
        'setDevice(self, QIODevice)'
        pass
    
    @classmethod
    def setFloatingPointPrecision(cls, self, QDataStreamFloatingPointPrecision):
        'setFloatingPointPrecision(self, QDataStream.FloatingPointPrecision)'
        pass
    
    @classmethod
    def setStatus(cls, self, QDataStreamStatus):
        'setStatus(self, QDataStream.Status)'
        pass
    
    @classmethod
    def setVersion(cls, self, int):
        'setVersion(self, int)'
        pass
    
    @classmethod
    def skipRawData(cls, self, int):
        'skipRawData(self, int) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    @classmethod
    def status(cls, self):
        'status(self) -> QDataStream.Status'
        pass
    
    @classmethod
    def version(cls, self):
        'version(self) -> int'
        return 1
    
    @classmethod
    def writeBool(cls, self, bool):
        'writeBool(self, bool)'
        pass
    
    @classmethod
    def writeBytes(cls, self, bytes):
        'writeBytes(self, bytes) -> QDataStream'
        pass
    
    @classmethod
    def writeDouble(cls, self, float):
        'writeDouble(self, float)'
        pass
    
    @classmethod
    def writeFloat(cls, self, float):
        'writeFloat(self, float)'
        pass
    
    @classmethod
    def writeInt(cls, self, int):
        'writeInt(self, int)'
        pass
    
    @classmethod
    def writeInt16(cls, self, int):
        'writeInt16(self, int)'
        pass
    
    @classmethod
    def writeInt32(cls, self, int):
        'writeInt32(self, int)'
        pass
    
    @classmethod
    def writeInt64(cls, self, int):
        'writeInt64(self, int)'
        pass
    
    @classmethod
    def writeInt8(cls, self, int):
        'writeInt8(self, int)'
        pass
    
    @classmethod
    def writeQString(cls, self, str):
        'writeQString(self, str)'
        pass
    
    @classmethod
    def writeQStringList(cls, self, Iterablestr=None):
        'writeQStringList(self, Iterable[str])'
        pass
    
    @classmethod
    def writeQVariant(cls, self, Any):
        'writeQVariant(self, Any)'
        pass
    
    @classmethod
    def writeQVariantHash(cls, self, Dictstr=None, Any=None):
        'writeQVariantHash(self, Dict[str, Any])'
        pass
    
    @classmethod
    def writeQVariantList(cls, self, ListAny=None):
        'writeQVariantList(self, List[Any])'
        pass
    
    @classmethod
    def writeQVariantMap(cls, self, Dictstr=None, Any=None):
        'writeQVariantMap(self, Dict[str, Any])'
        pass
    
    @classmethod
    def writeRawData(cls, self, bytes):
        'writeRawData(self, bytes) -> int'
        return 1
    
    @classmethod
    def writeString(cls, self, str):
        'writeString(self, str)'
        pass
    
    @classmethod
    def writeUInt16(cls, self, int):
        'writeUInt16(self, int)'
        pass
    
    @classmethod
    def writeUInt32(cls, self, int):
        'writeUInt32(self, int)'
        pass
    
    @classmethod
    def writeUInt64(cls, self, int):
        'writeUInt64(self, int)'
        pass
    
    @classmethod
    def writeUInt8(cls, self, int):
        'writeUInt8(self, int)'
        pass
    

class QDate(_mod_sip.simplewrapper):
    'QDate()\nQDate(int, int, int)\nQDate(QDate)'
    DateFormat = MonthNameType()
    MonthNameType = MonthNameType
    StandaloneFormat = MonthNameType()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QDate
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, int, int_, int_1):
        'QDate()\nQDate(int, int, int)\nQDate(QDate)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addDays(cls, self, int):
        'addDays(self, int) -> QDate'
        pass
    
    @classmethod
    def addMonths(cls, self, int):
        'addMonths(self, int) -> QDate'
        pass
    
    @classmethod
    def addYears(cls, self, int):
        'addYears(self, int) -> QDate'
        pass
    
    @classmethod
    def currentDate(cls):
        'currentDate() -> QDate'
        pass
    
    @classmethod
    def day(cls, self):
        'day(self) -> int'
        return 1
    
    @classmethod
    def dayOfWeek(cls, self):
        'dayOfWeek(self) -> int'
        return 1
    
    @classmethod
    def dayOfYear(cls, self):
        'dayOfYear(self) -> int'
        return 1
    
    @classmethod
    def daysInMonth(cls, self):
        'daysInMonth(self) -> int'
        return 1
    
    @classmethod
    def daysInYear(cls, self):
        'daysInYear(self) -> int'
        return 1
    
    @classmethod
    def daysTo(cls, self, UnionQDate=None, datetimedate=None):
        'daysTo(self, Union[QDate, datetime.date]) -> int'
        return 1
    
    @classmethod
    def fromJulianDay(cls, int):
        'fromJulianDay(int) -> QDate'
        pass
    
    @classmethod
    def fromString(cls, str, format: Qt.DateFormat=Qt.TextDate):
        'fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QDate\nfromString(str, str) -> QDate'
        pass
    
    @classmethod
    def getDate(cls, self):
        'getDate(self) -> Tuple[int, int, int]'
        pass
    
    @classmethod
    def isLeapYear(cls, int):
        'isLeapYear(int) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, int, int_, int_1):
        'isValid(self) -> bool\nisValid(int, int, int) -> bool'
        return True
    
    @classmethod
    def longDayName(cls, int, type: QDate.MonthNameType=QDate.DateFormat):
        'longDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str'
        return ''
    
    @classmethod
    def longMonthName(cls, int, type: QDate.MonthNameType=QDate.DateFormat):
        'longMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str'
        return ''
    
    @classmethod
    def month(cls, self):
        'month(self) -> int'
        return 1
    
    @classmethod
    def setDate(cls, self, int, int_, int_1):
        'setDate(self, int, int, int) -> bool'
        return True
    
    @classmethod
    def shortDayName(cls, int, type: QDate.MonthNameType=QDate.DateFormat):
        'shortDayName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str'
        return ''
    
    @classmethod
    def shortMonthName(cls, int, type: QDate.MonthNameType=QDate.DateFormat):
        'shortMonthName(int, type: QDate.MonthNameType = QDate.DateFormat) -> str'
        return ''
    
    @classmethod
    def toJulianDay(cls, self):
        'toJulianDay(self) -> int'
        return 1
    
    @classmethod
    def toPyDate(cls, self):
        'toPyDate(self) -> datetime.date'
        pass
    
    @classmethod
    def toString(cls, self, format: Qt.DateFormat=Qt.TextDate):
        'toString(self, format: Qt.DateFormat = Qt.TextDate) -> str\ntoString(self, str) -> str'
        return ''
    
    @classmethod
    def weekNumber(cls, self):
        'weekNumber(self) -> Tuple[int, int]'
        pass
    
    @classmethod
    def year(cls, self):
        'year(self) -> int'
        return 1
    

class QDateTime(_mod_sip.simplewrapper):
    'QDateTime()\nQDateTime(Union[QDateTime, datetime.datetime])\nQDateTime(Union[QDate, datetime.date])\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)\nQDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], Qt.TimeSpec, int)\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], QTimeZone)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QDateTime
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, UnionQDate=None, datetimedate=None, UnionQTime=None, datetimetime=None, timeSpec: Qt.TimeSpec=Qt.LocalTime):
        'QDateTime()\nQDateTime(Union[QDateTime, datetime.datetime])\nQDateTime(Union[QDate, datetime.date])\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], timeSpec: Qt.TimeSpec = Qt.LocalTime)\nQDateTime(int, int, int, int, int, second: int = 0, msec: int = 0, timeSpec: int = 0)\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], Qt.TimeSpec, int)\nQDateTime(Union[QDate, datetime.date], Union[QTime, datetime.time], QTimeZone)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addDays(cls, self, int):
        'addDays(self, int) -> QDateTime'
        pass
    
    @classmethod
    def addMSecs(cls, self, int):
        'addMSecs(self, int) -> QDateTime'
        pass
    
    @classmethod
    def addMonths(cls, self, int):
        'addMonths(self, int) -> QDateTime'
        pass
    
    @classmethod
    def addSecs(cls, self, int):
        'addSecs(self, int) -> QDateTime'
        pass
    
    @classmethod
    def addYears(cls, self, int):
        'addYears(self, int) -> QDateTime'
        pass
    
    @classmethod
    def currentDateTime(cls):
        'currentDateTime() -> QDateTime'
        pass
    
    @classmethod
    def currentDateTimeUtc(cls):
        'currentDateTimeUtc() -> QDateTime'
        pass
    
    @classmethod
    def currentMSecsSinceEpoch(cls):
        'currentMSecsSinceEpoch() -> int'
        return 1
    
    @classmethod
    def currentSecsSinceEpoch(cls):
        'currentSecsSinceEpoch() -> int'
        return 1
    
    @classmethod
    def date(cls, self):
        'date(self) -> QDate'
        pass
    
    @classmethod
    def daysTo(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'daysTo(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def fromMSecsSinceEpoch(cls, int, QtTimeSpec, offsetSeconds: int=0):
        'fromMSecsSinceEpoch(int) -> QDateTime\nfromMSecsSinceEpoch(int, Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime\nfromMSecsSinceEpoch(int, QTimeZone) -> QDateTime'
        pass
    
    @classmethod
    def fromSecsSinceEpoch(cls, int, spec: Qt.TimeSpec=Qt.TimeSpec.LocalTime, offsetSeconds: int=0):
        'fromSecsSinceEpoch(int, spec: Qt.TimeSpec = Qt.TimeSpec.LocalTime, offsetSeconds: int = 0) -> QDateTime\nfromSecsSinceEpoch(int, QTimeZone) -> QDateTime'
        pass
    
    @classmethod
    def fromString(cls, str, format: Qt.DateFormat=Qt.TextDate):
        'fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QDateTime\nfromString(str, str) -> QDateTime'
        pass
    
    @classmethod
    def fromTime_t(cls, int, QtTimeSpec, offsetSeconds: int=0):
        'fromTime_t(int) -> QDateTime\nfromTime_t(int, Qt.TimeSpec, offsetSeconds: int = 0) -> QDateTime\nfromTime_t(int, QTimeZone) -> QDateTime'
        pass
    
    @classmethod
    def isDaylightTime(cls, self):
        'isDaylightTime(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def msecsTo(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'msecsTo(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def offsetFromUtc(cls, self):
        'offsetFromUtc(self) -> int'
        return 1
    
    @classmethod
    def secsTo(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'secsTo(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def setDate(cls, self, UnionQDate=None, datetimedate=None):
        'setDate(self, Union[QDate, datetime.date])'
        pass
    
    @classmethod
    def setMSecsSinceEpoch(cls, self, int):
        'setMSecsSinceEpoch(self, int)'
        pass
    
    @classmethod
    def setOffsetFromUtc(cls, self, int):
        'setOffsetFromUtc(self, int)'
        pass
    
    @classmethod
    def setSecsSinceEpoch(cls, self, int):
        'setSecsSinceEpoch(self, int)'
        pass
    
    @classmethod
    def setTime(cls, self, UnionQTime=None, datetimetime=None):
        'setTime(self, Union[QTime, datetime.time])'
        pass
    
    @classmethod
    def setTimeSpec(cls, self, QtTimeSpec):
        'setTimeSpec(self, Qt.TimeSpec)'
        pass
    
    @classmethod
    def setTimeZone(cls, self, QTimeZone):
        'setTimeZone(self, QTimeZone)'
        pass
    
    @classmethod
    def setTime_t(cls, self, int):
        'setTime_t(self, int)'
        pass
    
    @classmethod
    def swap(cls, self, QDateTime):
        'swap(self, QDateTime)'
        pass
    
    @classmethod
    def time(cls, self):
        'time(self) -> QTime'
        pass
    
    @classmethod
    def timeSpec(cls, self):
        'timeSpec(self) -> Qt.TimeSpec'
        pass
    
    @classmethod
    def timeZone(cls, self):
        'timeZone(self) -> QTimeZone'
        pass
    
    @classmethod
    def timeZoneAbbreviation(cls, self):
        'timeZoneAbbreviation(self) -> str'
        return ''
    
    @classmethod
    def toLocalTime(cls, self):
        'toLocalTime(self) -> QDateTime'
        pass
    
    @classmethod
    def toMSecsSinceEpoch(cls, self):
        'toMSecsSinceEpoch(self) -> int'
        return 1
    
    @classmethod
    def toOffsetFromUtc(cls, self, int):
        'toOffsetFromUtc(self, int) -> QDateTime'
        pass
    
    @classmethod
    def toPyDateTime(cls, self):
        'toPyDateTime(self) -> datetime.datetime'
        pass
    
    @classmethod
    def toSecsSinceEpoch(cls, self):
        'toSecsSinceEpoch(self) -> int'
        return 1
    
    @classmethod
    def toString(cls, self, format: Qt.DateFormat=Qt.TextDate):
        'toString(self, format: Qt.DateFormat = Qt.TextDate) -> str\ntoString(self, str) -> str'
        return ''
    
    @classmethod
    def toTimeSpec(cls, self, QtTimeSpec):
        'toTimeSpec(self, Qt.TimeSpec) -> QDateTime'
        pass
    
    @classmethod
    def toTimeZone(cls, self, QTimeZone):
        'toTimeZone(self, QTimeZone) -> QDateTime'
        pass
    
    @classmethod
    def toTime_t(cls, self):
        'toTime_t(self) -> int'
        return 1
    
    @classmethod
    def toUTC(cls, self):
        'toUTC(self) -> QDateTime'
        pass
    

class QDeadlineTimer(_mod_sip.simplewrapper):
    'QDeadlineTimer(type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(QDeadlineTimer.ForeverConstant, type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(int, type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(QDeadlineTimer)'
    Forever = ForeverConstant()
    ForeverConstant = ForeverConstant
    def __add__(self, value):
        'Return self+value.'
        return QDeadlineTimer()
    
    __class__ = QDeadlineTimer
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __init__(self, QDeadlineTimerForeverConstant, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'QDeadlineTimer(type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(QDeadlineTimer.ForeverConstant, type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(int, type: Qt.TimerType = Qt.TimerType.CoarseTimer)\nQDeadlineTimer(QDeadlineTimer)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QDeadlineTimer()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QDeadlineTimer()
    
    def __sub__(self, value):
        'Return self-value.'
        return QDeadlineTimer()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addNSecs(cls, QDeadlineTimer, int):
        'addNSecs(QDeadlineTimer, int) -> QDeadlineTimer'
        pass
    
    @classmethod
    def current(cls, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'current(type: Qt.TimerType = Qt.TimerType.CoarseTimer) -> QDeadlineTimer'
        pass
    
    @classmethod
    def deadline(cls, self):
        'deadline(self) -> int'
        return 1
    
    @classmethod
    def deadlineNSecs(cls, self):
        'deadlineNSecs(self) -> int'
        return 1
    
    @classmethod
    def hasExpired(cls, self):
        'hasExpired(self) -> bool'
        return True
    
    @classmethod
    def isForever(cls, self):
        'isForever(self) -> bool'
        return True
    
    @classmethod
    def remainingTime(cls, self):
        'remainingTime(self) -> int'
        return 1
    
    @classmethod
    def remainingTimeNSecs(cls, self):
        'remainingTimeNSecs(self) -> int'
        return 1
    
    @classmethod
    def setDeadline(cls, self, int, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'setDeadline(self, int, type: Qt.TimerType = Qt.TimerType.CoarseTimer)'
        pass
    
    @classmethod
    def setPreciseDeadline(cls, self, int, nsecs: int=0, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'setPreciseDeadline(self, int, nsecs: int = 0, type: Qt.TimerType = Qt.TimerType.CoarseTimer)'
        pass
    
    @classmethod
    def setPreciseRemainingTime(cls, self, int, nsecs: int=0, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'setPreciseRemainingTime(self, int, nsecs: int = 0, type: Qt.TimerType = Qt.TimerType.CoarseTimer)'
        pass
    
    @classmethod
    def setRemainingTime(cls, self, int, type: Qt.TimerType=Qt.TimerType.CoarseTimer):
        'setRemainingTime(self, int, type: Qt.TimerType = Qt.TimerType.CoarseTimer)'
        pass
    
    @classmethod
    def setTimerType(cls, self, QtTimerType):
        'setTimerType(self, Qt.TimerType)'
        pass
    
    @classmethod
    def swap(cls, self, QDeadlineTimer):
        'swap(self, QDeadlineTimer)'
        pass
    
    @classmethod
    def timerType(cls, self):
        'timerType(self) -> Qt.TimerType'
        pass
    

class QDir(_mod_sip.simplewrapper):
    "QDir(QDir)\nQDir(path: str = '')\nQDir(str, str, sort: QDir.SortFlags = QDir.Name|QDir.IgnoreCase, filters: QDir.Filters = QDir.AllEntries)"
    AccessMask = Filter()
    AllDirs = Filter()
    AllEntries = Filter()
    CaseSensitive = Filter()
    Dirs = Filter()
    DirsFirst = SortFlag()
    DirsLast = SortFlag()
    Drives = Filter()
    Executable = Filter()
    Files = Filter()
    Filter = Filter
    Filters = Filters
    Hidden = Filter()
    IgnoreCase = SortFlag()
    LocaleAware = SortFlag()
    Modified = Filter()
    Name = SortFlag()
    NoDot = Filter()
    NoDotAndDotDot = Filter()
    NoDotDot = Filter()
    NoFilter = Filter()
    NoSort = SortFlag()
    NoSymLinks = Filter()
    PermissionMask = Filter()
    Readable = Filter()
    Reversed = SortFlag()
    Size = SortFlag()
    SortByMask = SortFlag()
    SortFlag = SortFlag
    SortFlags = SortFlags
    System = Filter()
    Time = SortFlag()
    Type = SortFlag()
    TypeMask = Filter()
    Unsorted = SortFlag()
    Writable = Filter()
    __class__ = QDir
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, str, str_, sort: QDir.SortFlags=QDir.Name|QDir.IgnoreCase, filters: QDir.Filters=QDir.AllEntries):
        "QDir(QDir)\nQDir(path: str = '')\nQDir(str, str, sort: QDir.SortFlags = QDir.Name|QDir.IgnoreCase, filters: QDir.Filters = QDir.AllEntries)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def absoluteFilePath(cls, self, str):
        'absoluteFilePath(self, str) -> str'
        return ''
    
    @classmethod
    def absolutePath(cls, self):
        'absolutePath(self) -> str'
        return ''
    
    @classmethod
    def addSearchPath(cls, str, str_):
        'addSearchPath(str, str)'
        pass
    
    @classmethod
    def canonicalPath(cls, self):
        'canonicalPath(self) -> str'
        return ''
    
    @classmethod
    def cd(cls, self, str):
        'cd(self, str) -> bool'
        return True
    
    @classmethod
    def cdUp(cls, self):
        'cdUp(self) -> bool'
        return True
    
    @classmethod
    def cleanPath(cls, str):
        'cleanPath(str) -> str'
        return ''
    
    @classmethod
    def count(cls, self):
        'count(self) -> int'
        return 1
    
    @classmethod
    def current(cls):
        'current() -> QDir'
        pass
    
    @classmethod
    def currentPath(cls):
        'currentPath() -> str'
        return ''
    
    @classmethod
    def dirName(cls, self):
        'dirName(self) -> str'
        return ''
    
    @classmethod
    def drives(cls):
        'drives() -> object'
        pass
    
    @classmethod
    def entryInfoList(cls, self, Iterablestr=None, filters: Union[QDir.Filters,QDir.Filter]=QDir.NoFilter, sort: Union[QDir.SortFlags,QDir.SortFlag]=QDir.NoSort):
        'entryInfoList(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.NoSort) -> object\nentryInfoList(self, Iterable[str], filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.NoSort) -> object'
        pass
    
    @classmethod
    def entryList(cls, self, Iterablestr=None, filters: Union[QDir.Filters,QDir.Filter]=QDir.NoFilter, sort: Union[QDir.SortFlags,QDir.SortFlag]=QDir.NoSort):
        'entryList(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.NoSort) -> List[str]\nentryList(self, Iterable[str], filters: Union[QDir.Filters, QDir.Filter] = QDir.NoFilter, sort: Union[QDir.SortFlags, QDir.SortFlag] = QDir.NoSort) -> List[str]'
        pass
    
    @classmethod
    def exists(cls, self, str):
        'exists(self) -> bool\nexists(self, str) -> bool'
        return True
    
    @classmethod
    def filePath(cls, self, str):
        'filePath(self, str) -> str'
        return ''
    
    @classmethod
    def filter(cls, self):
        'filter(self) -> QDir.Filters'
        pass
    
    @classmethod
    def fromNativeSeparators(cls, str):
        'fromNativeSeparators(str) -> str'
        return ''
    
    @classmethod
    def home(cls):
        'home() -> QDir'
        pass
    
    @classmethod
    def homePath(cls):
        'homePath() -> str'
        return ''
    
    @classmethod
    def isAbsolute(cls, self):
        'isAbsolute(self) -> bool'
        return True
    
    @classmethod
    def isAbsolutePath(cls, str):
        'isAbsolutePath(str) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self, filters: Union[QDir.Filters,QDir.Filter]=QDir.AllEntries|QDir.NoDotAndDotDot):
        'isEmpty(self, filters: Union[QDir.Filters, QDir.Filter] = QDir.AllEntries|QDir.NoDotAndDotDot) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isRelative(cls, self):
        'isRelative(self) -> bool'
        return True
    
    @classmethod
    def isRelativePath(cls, str):
        'isRelativePath(str) -> bool'
        return True
    
    @classmethod
    def isRoot(cls, self):
        'isRoot(self) -> bool'
        return True
    
    @classmethod
    def listSeparator(cls):
        'listSeparator() -> str'
        return ''
    
    @classmethod
    def makeAbsolute(cls, self):
        'makeAbsolute(self) -> bool'
        return True
    
    @classmethod
    def match(cls, Iterablestr=None, str=None):
        'match(Iterable[str], str) -> bool\nmatch(str, str) -> bool'
        return True
    
    @classmethod
    def mkdir(cls, self, str):
        'mkdir(self, str) -> bool'
        return True
    
    @classmethod
    def mkpath(cls, self, str):
        'mkpath(self, str) -> bool'
        return True
    
    @classmethod
    def nameFilters(cls, self):
        'nameFilters(self) -> List[str]'
        pass
    
    @classmethod
    def nameFiltersFromString(cls, str):
        'nameFiltersFromString(str) -> List[str]'
        pass
    
    @classmethod
    def path(cls, self):
        'path(self) -> str'
        return ''
    
    @classmethod
    def refresh(cls, self):
        'refresh(self)'
        pass
    
    @classmethod
    def relativeFilePath(cls, self, str):
        'relativeFilePath(self, str) -> str'
        return ''
    
    @classmethod
    def remove(cls, self, str):
        'remove(self, str) -> bool'
        return True
    
    @classmethod
    def removeRecursively(cls, self):
        'removeRecursively(self) -> bool'
        return True
    
    @classmethod
    def rename(cls, self, str, str_):
        'rename(self, str, str) -> bool'
        return True
    
    @classmethod
    def rmdir(cls, self, str):
        'rmdir(self, str) -> bool'
        return True
    
    @classmethod
    def rmpath(cls, self, str):
        'rmpath(self, str) -> bool'
        return True
    
    @classmethod
    def root(cls):
        'root() -> QDir'
        pass
    
    @classmethod
    def rootPath(cls):
        'rootPath() -> str'
        return ''
    
    @classmethod
    def searchPaths(cls, str):
        'searchPaths(str) -> List[str]'
        pass
    
    @classmethod
    def separator(cls):
        'separator() -> str'
        return ''
    
    @classmethod
    def setCurrent(cls, str):
        'setCurrent(str) -> bool'
        return True
    
    @classmethod
    def setFilter(cls, self, UnionQDirFilters=None, QDirFilter=None):
        'setFilter(self, Union[QDir.Filters, QDir.Filter])'
        pass
    
    @classmethod
    def setNameFilters(cls, self, Iterablestr=None):
        'setNameFilters(self, Iterable[str])'
        pass
    
    @classmethod
    def setPath(cls, self, str):
        'setPath(self, str)'
        pass
    
    @classmethod
    def setSearchPaths(cls, str, Iterablestr=None):
        'setSearchPaths(str, Iterable[str])'
        pass
    
    @classmethod
    def setSorting(cls, self, UnionQDirSortFlags=None, QDirSortFlag=None):
        'setSorting(self, Union[QDir.SortFlags, QDir.SortFlag])'
        pass
    
    @classmethod
    def sorting(cls, self):
        'sorting(self) -> QDir.SortFlags'
        pass
    
    @classmethod
    def swap(cls, self, QDir):
        'swap(self, QDir)'
        pass
    
    @classmethod
    def temp(cls):
        'temp() -> QDir'
        pass
    
    @classmethod
    def tempPath(cls):
        'tempPath() -> str'
        return ''
    
    @classmethod
    def toNativeSeparators(cls, str):
        'toNativeSeparators(str) -> str'
        return ''
    

class QDirIterator(_mod_sip.simplewrapper):
    'QDirIterator(QDir, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, QDir.Filters, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, Iterable[str], filters: QDir.Filters = QDir.NoFilter, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)'
    FollowSymlinks = IteratorFlag()
    IteratorFlag = IteratorFlag
    IteratorFlags = IteratorFlags
    NoIteratorFlags = IteratorFlag()
    Subdirectories = IteratorFlag()
    __class__ = QDirIterator
    __dict__ = {}
    def __init__(self, str, Iterablestr=None, filters: QDir.Filters=QDir.NoFilter, flags: QDirIterator.IteratorFlags=QDirIterator.NoIteratorFlags):
        'QDirIterator(QDir, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, QDir.Filters, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)\nQDirIterator(str, Iterable[str], filters: QDir.Filters = QDir.NoFilter, flags: QDirIterator.IteratorFlags = QDirIterator.NoIteratorFlags)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def fileInfo(cls, self):
        'fileInfo(self) -> QFileInfo'
        pass
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def filePath(cls, self):
        'filePath(self) -> str'
        return ''
    
    @classmethod
    def hasNext(cls, self):
        'hasNext(self) -> bool'
        return True
    
    @classmethod
    def next(cls, self):
        'next(self) -> str'
        return ''
    
    @classmethod
    def path(cls, self):
        'path(self) -> str'
        return ''
    

class QDynamicPropertyChangeEvent(QEvent):
    'QDynamicPropertyChangeEvent(Union[QByteArray, bytes, bytearray])\nQDynamicPropertyChangeEvent(QDynamicPropertyChangeEvent)'
    __class__ = QDynamicPropertyChangeEvent
    __dict__ = {}
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None):
        'QDynamicPropertyChangeEvent(Union[QByteArray, bytes, bytearray])\nQDynamicPropertyChangeEvent(QDynamicPropertyChangeEvent)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def accept(cls, self):
        'accept(self)'
        pass
    
    @classmethod
    def ignore(cls, self):
        'ignore(self)'
        pass
    
    @classmethod
    def isAccepted(cls, self):
        'isAccepted(self) -> bool'
        return True
    
    @classmethod
    def propertyName(cls, self):
        'propertyName(self) -> QByteArray'
        pass
    
    @classmethod
    def registerEventType(cls, hint: int=-1):
        'registerEventType(hint: int = -1) -> int'
        return 1
    
    @classmethod
    def setAccepted(cls, self, bool):
        'setAccepted(self, bool)'
        pass
    
    @classmethod
    def spontaneous(cls, self):
        'spontaneous(self) -> bool'
        return True
    
    @classmethod
    def type(cls, self):
        'type(self) -> QEvent.Type'
        pass
    

class QEasingCurve(_mod_sip.simplewrapper):
    'QEasingCurve(type: QEasingCurve.Type = QEasingCurve.Linear)\nQEasingCurve(Union[QEasingCurve, QEasingCurve.Type])'
    BezierSpline = Type()
    CosineCurve = Type()
    Custom = Type()
    InBack = Type()
    InBounce = Type()
    InCirc = Type()
    InCubic = Type()
    InCurve = Type()
    InElastic = Type()
    InExpo = Type()
    InOutBack = Type()
    InOutBounce = Type()
    InOutCirc = Type()
    InOutCubic = Type()
    InOutElastic = Type()
    InOutExpo = Type()
    InOutQuad = Type()
    InOutQuart = Type()
    InOutQuint = Type()
    InOutSine = Type()
    InQuad = Type()
    InQuart = Type()
    InQuint = Type()
    InSine = Type()
    Linear = Type()
    OutBack = Type()
    OutBounce = Type()
    OutCirc = Type()
    OutCubic = Type()
    OutCurve = Type()
    OutElastic = Type()
    OutExpo = Type()
    OutInBack = Type()
    OutInBounce = Type()
    OutInCirc = Type()
    OutInCubic = Type()
    OutInElastic = Type()
    OutInExpo = Type()
    OutInQuad = Type()
    OutInQuart = Type()
    OutInQuint = Type()
    OutInSine = Type()
    OutQuad = Type()
    OutQuart = Type()
    OutQuint = Type()
    OutSine = Type()
    SineCurve = Type()
    TCBSpline = Type()
    Type = Type
    __class__ = QEasingCurve
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, type: QEasingCurve.Type=QEasingCurve.Linear):
        'QEasingCurve(type: QEasingCurve.Type = QEasingCurve.Linear)\nQEasingCurve(Union[QEasingCurve, QEasingCurve.Type])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addCubicBezierSegment(cls, self, UnionQPointF=None, QPoint=None, UnionQPointF_=None, QPoint_=None, UnionQPointF_1=None, QPoint_1=None):
        'addCubicBezierSegment(self, Union[QPointF, QPoint], Union[QPointF, QPoint], Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def addTCBSegment(cls, self, UnionQPointF=None, QPoint=None, float=None, float_=None, float_1=None):
        'addTCBSegment(self, Union[QPointF, QPoint], float, float, float)'
        pass
    
    @classmethod
    def amplitude(cls, self):
        'amplitude(self) -> float'
        return 1.0
    
    @classmethod
    def customType(cls, self):
        'customType(self) -> Callable[[], float]'
        pass
    
    @classmethod
    def overshoot(cls, self):
        'overshoot(self) -> float'
        return 1.0
    
    @classmethod
    def period(cls, self):
        'period(self) -> float'
        return 1.0
    
    @classmethod
    def setAmplitude(cls, self, float):
        'setAmplitude(self, float)'
        pass
    
    @classmethod
    def setCustomType(cls, self, Callable, float):
        'setCustomType(self, Callable[[], float])'
        pass
    
    @classmethod
    def setOvershoot(cls, self, float):
        'setOvershoot(self, float)'
        pass
    
    @classmethod
    def setPeriod(cls, self, float):
        'setPeriod(self, float)'
        pass
    
    @classmethod
    def setType(cls, self, QEasingCurveType):
        'setType(self, QEasingCurve.Type)'
        pass
    
    @classmethod
    def swap(cls, self, QEasingCurve):
        'swap(self, QEasingCurve)'
        pass
    
    @classmethod
    def toCubicSpline(cls, self):
        'toCubicSpline(self) -> object'
        pass
    
    @classmethod
    def type(cls, self):
        'type(self) -> QEasingCurve.Type'
        pass
    
    @classmethod
    def valueForProgress(cls, self, float):
        'valueForProgress(self, float) -> float'
        return 1.0
    

class QElapsedTimer(_mod_sip.simplewrapper):
    'QElapsedTimer()\nQElapsedTimer(QElapsedTimer)'
    ClockType = ClockType
    MachAbsoluteTime = ClockType()
    MonotonicClock = ClockType()
    PerformanceCounter = ClockType()
    SystemTime = ClockType()
    TickCounter = ClockType()
    __class__ = QElapsedTimer
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QElapsedTimer):
        'QElapsedTimer()\nQElapsedTimer(QElapsedTimer)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def clockType(cls):
        'clockType() -> QElapsedTimer.ClockType'
        pass
    
    @classmethod
    def elapsed(cls, self):
        'elapsed(self) -> int'
        return 1
    
    @classmethod
    def hasExpired(cls, self, int):
        'hasExpired(self, int) -> bool'
        return True
    
    @classmethod
    def invalidate(cls, self):
        'invalidate(self)'
        pass
    
    @classmethod
    def isMonotonic(cls):
        'isMonotonic() -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def msecsSinceReference(cls, self):
        'msecsSinceReference(self) -> int'
        return 1
    
    @classmethod
    def msecsTo(cls, self, QElapsedTimer):
        'msecsTo(self, QElapsedTimer) -> int'
        return 1
    
    @classmethod
    def nsecsElapsed(cls, self):
        'nsecsElapsed(self) -> int'
        return 1
    
    @classmethod
    def restart(cls, self):
        'restart(self) -> int'
        return 1
    
    @classmethod
    def secsTo(cls, self, QElapsedTimer):
        'secsTo(self, QElapsedTimer) -> int'
        return 1
    
    @classmethod
    def start(cls, self):
        'start(self)'
        pass
    

class QEvent(_mod_sip.wrapper):
    'QEvent(QEvent.Type)\nQEvent(QEvent)'
    ActionAdded = Type()
    ActionChanged = Type()
    ActionRemoved = Type()
    ActivationChange = Type()
    ApplicationActivate = Type()
    ApplicationActivated = Type()
    ApplicationDeactivate = Type()
    ApplicationDeactivated = Type()
    ApplicationFontChange = Type()
    ApplicationLayoutDirectionChange = Type()
    ApplicationPaletteChange = Type()
    ApplicationStateChange = Type()
    ApplicationWindowIconChange = Type()
    ChildAdded = Type()
    ChildPolished = Type()
    ChildRemoved = Type()
    Clipboard = Type()
    Close = Type()
    CloseSoftwareInputPanel = Type()
    ContentsRectChange = Type()
    ContextMenu = Type()
    CursorChange = Type()
    DeferredDelete = Type()
    DragEnter = Type()
    DragLeave = Type()
    DragMove = Type()
    Drop = Type()
    DynamicPropertyChange = Type()
    EnabledChange = Type()
    Enter = Type()
    EnterWhatsThisMode = Type()
    Expose = Type()
    FileOpen = Type()
    FocusAboutToChange = Type()
    FocusIn = Type()
    FocusOut = Type()
    FontChange = Type()
    Gesture = Type()
    GestureOverride = Type()
    GrabKeyboard = Type()
    GrabMouse = Type()
    GraphicsSceneContextMenu = Type()
    GraphicsSceneDragEnter = Type()
    GraphicsSceneDragLeave = Type()
    GraphicsSceneDragMove = Type()
    GraphicsSceneDrop = Type()
    GraphicsSceneHelp = Type()
    GraphicsSceneHoverEnter = Type()
    GraphicsSceneHoverLeave = Type()
    GraphicsSceneHoverMove = Type()
    GraphicsSceneMouseDoubleClick = Type()
    GraphicsSceneMouseMove = Type()
    GraphicsSceneMousePress = Type()
    GraphicsSceneMouseRelease = Type()
    GraphicsSceneMove = Type()
    GraphicsSceneResize = Type()
    GraphicsSceneWheel = Type()
    Hide = Type()
    HideToParent = Type()
    HoverEnter = Type()
    HoverLeave = Type()
    HoverMove = Type()
    IconDrag = Type()
    IconTextChange = Type()
    InputMethod = Type()
    InputMethodQuery = Type()
    KeyPress = Type()
    KeyRelease = Type()
    KeyboardLayoutChange = Type()
    LanguageChange = Type()
    LayoutDirectionChange = Type()
    LayoutRequest = Type()
    Leave = Type()
    LeaveWhatsThisMode = Type()
    LocaleChange = Type()
    MacSizeChange = Type()
    MaxUser = Type()
    MetaCall = Type()
    ModifiedChange = Type()
    MouseButtonDblClick = Type()
    MouseButtonPress = Type()
    MouseButtonRelease = Type()
    MouseMove = Type()
    MouseTrackingChange = Type()
    Move = Type()
    NonClientAreaMouseButtonDblClick = Type()
    NonClientAreaMouseButtonPress = Type()
    NonClientAreaMouseButtonRelease = Type()
    NonClientAreaMouseMove = Type()
    None_ = Type()
    OkRequest = Type()
    OrientationChange = Type()
    Paint = Type()
    PaletteChange = Type()
    ParentAboutToChange = Type()
    ParentChange = Type()
    PlatformPanel = Type()
    PlatformSurface = Type()
    Polish = Type()
    PolishRequest = Type()
    QueryWhatsThis = Type()
    ReadOnlyChange = Type()
    RequestSoftwareInputPanel = Type()
    Resize = Type()
    Scroll = Type()
    ScrollPrepare = Type()
    Shortcut = Type()
    ShortcutOverride = Type()
    Show = Type()
    ShowToParent = Type()
    SockAct = Type()
    StateMachineSignal = Type()
    StateMachineWrapped = Type()
    StatusTip = Type()
    StyleChange = Type()
    TabletEnterProximity = Type()
    TabletLeaveProximity = Type()
    TabletMove = Type()
    TabletPress = Type()
    TabletRelease = Type()
    TabletTrackingChange = Type()
    ThreadChange = Type()
    Timer = Type()
    ToolBarChange = Type()
    ToolTip = Type()
    ToolTipChange = Type()
    TouchBegin = Type()
    TouchCancel = Type()
    TouchEnd = Type()
    TouchUpdate = Type()
    Type = Type
    UngrabKeyboard = Type()
    UngrabMouse = Type()
    UpdateLater = Type()
    UpdateRequest = Type()
    User = Type()
    WhatsThis = Type()
    WhatsThisClicked = Type()
    Wheel = Type()
    WinEventAct = Type()
    WinIdChange = Type()
    WindowActivate = Type()
    WindowBlocked = Type()
    WindowDeactivate = Type()
    WindowIconChange = Type()
    WindowStateChange = Type()
    WindowTitleChange = Type()
    WindowUnblocked = Type()
    ZOrderChange = Type()
    __class__ = QEvent
    __dict__ = {}
    def __init__(self, QEventType):
        'QEvent(QEvent.Type)\nQEvent(QEvent)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def accept(cls, self):
        'accept(self)'
        pass
    
    @classmethod
    def ignore(cls, self):
        'ignore(self)'
        pass
    
    @classmethod
    def isAccepted(cls, self):
        'isAccepted(self) -> bool'
        return True
    
    @classmethod
    def registerEventType(cls, hint: int=-1):
        'registerEventType(hint: int = -1) -> int'
        return 1
    
    @classmethod
    def setAccepted(cls, self, bool):
        'setAccepted(self, bool)'
        pass
    
    @classmethod
    def spontaneous(cls, self):
        'spontaneous(self) -> bool'
        return True
    
    @classmethod
    def type(cls, self):
        'type(self) -> QEvent.Type'
        pass
    

class QEventLoop(QObject):
    'QEventLoop(parent: QObject = None)'
    AllEvents = ProcessEventsFlag()
    ExcludeSocketNotifiers = ProcessEventsFlag()
    ExcludeUserInputEvents = ProcessEventsFlag()
    ProcessEventsFlag = ProcessEventsFlag
    ProcessEventsFlags = ProcessEventsFlags
    WaitForMoreEvents = ProcessEventsFlag()
    X11ExcludeTimers = ProcessEventsFlag()
    __class__ = QEventLoop
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QEventLoop(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def exec(cls, self, flags: QEventLoop.ProcessEventsFlags=QEventLoop.AllEvents):
        'exec(self, flags: QEventLoop.ProcessEventsFlags = QEventLoop.AllEvents) -> int'
        return 1
    
    @classmethod
    def exec_(cls, self, flags: QEventLoop.ProcessEventsFlags=QEventLoop.AllEvents):
        'exec_(self, flags: QEventLoop.ProcessEventsFlags = QEventLoop.AllEvents) -> int'
        return 1
    
    @classmethod
    def exit(cls, self, returnCode: int=0):
        'exit(self, returnCode: int = 0)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isRunning(cls, self):
        'isRunning(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def processEvents(cls, self, flags: Union[QEventLoop.ProcessEventsFlags,QEventLoop.ProcessEventsFlag]=QEventLoop.AllEvents):
        'processEvents(self, flags: Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag] = QEventLoop.AllEvents) -> bool\nprocessEvents(self, Union[QEventLoop.ProcessEventsFlags, QEventLoop.ProcessEventsFlag], int)'
        return True
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def quit(cls, self):
        'quit(self)'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def wakeUp(cls, self):
        'wakeUp(self)'
        pass
    

class QEventLoopLocker(_mod_sip.simplewrapper):
    'QEventLoopLocker()\nQEventLoopLocker(QEventLoop)\nQEventLoopLocker(QThread)'
    __class__ = QEventLoopLocker
    __dict__ = {}
    def __init__(self, QEventLoop):
        'QEventLoopLocker()\nQEventLoopLocker(QEventLoop)\nQEventLoopLocker(QThread)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class QEventTransition(QAbstractTransition):
    'QEventTransition(sourceState: QState = None)\nQEventTransition(QObject, QEvent.Type, sourceState: QState = None)'
    __class__ = QEventTransition
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QObject, QEventType, sourceState: QState=None):
        'QEventTransition(sourceState: QState = None)\nQEventTransition(QObject, QEvent.Type, sourceState: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def animations(cls, self):
        'animations(self) -> object'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def eventSource(cls, self):
        'eventSource(self) -> QObject'
        pass
    
    @classmethod
    def eventTest(cls, self, QEvent):
        'eventTest(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventType(cls, self):
        'eventType(self) -> QEvent.Type'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onTransition(cls, self, QEvent):
        'onTransition(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setEventSource(cls, self, QObject):
        'setEventSource(self, QObject)'
        pass
    
    @classmethod
    def setEventType(cls, self, QEventType):
        'setEventType(self, QEvent.Type)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTargetState(cls, self, QAbstractState):
        'setTargetState(self, QAbstractState)'
        pass
    
    @classmethod
    def setTargetStates(cls, self, IterableQAbstractState=None):
        'setTargetStates(self, Iterable[QAbstractState])'
        pass
    
    @classmethod
    def setTransitionType(cls, self, QAbstractTransitionTransitionType):
        'setTransitionType(self, QAbstractTransition.TransitionType)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sourceState(cls, self):
        'sourceState(self) -> QState'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def targetState(cls, self):
        'targetState(self) -> QAbstractState'
        pass
    
    @classmethod
    def targetStates(cls, self):
        'targetStates(self) -> object'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transitionType(cls, self):
        'transitionType(self) -> QAbstractTransition.TransitionType'
        pass
    

class QFile(QFileDevice):
    'QFile()\nQFile(str)\nQFile(QObject)\nQFile(str, QObject)'
    __class__ = QFile
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, QObject):
        'QFile()\nQFile(str)\nQFile(QObject)\nQFile(str, QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def copy(cls, self, str):
        'copy(self, str) -> bool\ncopy(str, str) -> bool'
        return True
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def decodeName(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'decodeName(Union[QByteArray, bytes, bytearray]) -> str\ndecodeName(str) -> str'
        return ''
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeName(cls, str):
        'encodeName(str) -> QByteArray'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QFileDevice.FileError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def exists(cls, self):
        'exists(self) -> bool\nexists(str) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls, self):
        'flush(self) -> bool'
        return True
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def handle(cls, self):
        'handle(self) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def link(cls, self, str):
        'link(self, str) -> bool\nlink(str, str) -> bool'
        return True
    
    @classmethod
    def map(cls, self, int, int_, flags: QFileDevice.MemoryMapFlags=QFileDevice.NoOptions):
        'map(self, int, int, flags: QFileDevice.MemoryMapFlags = QFileDevice.NoOptions) -> sip.voidptr'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, int, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None, handleFlags: Union[QFileDevice.FileHandleFlags,QFileDevice.FileHandleFlag]=QFileDevice.DontCloseHandle):
        'open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool\nopen(self, int, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag], handleFlags: Union[QFileDevice.FileHandleFlags, QFileDevice.FileHandleFlag] = QFileDevice.DontCloseHandle) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def permissions(cls, self):
        'permissions(self) -> QFileDevice.Permissions\npermissions(str) -> QFileDevice.Permissions'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls):
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls):
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def remove(cls, self):
        'remove(self) -> bool\nremove(str) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def rename(cls, self, str):
        'rename(self, str) -> bool\nrename(str, str) -> bool'
        return True
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int) -> bool\nresize(str, int) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setErrorString(cls):
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls):
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPermissions(cls, self, UnionQFileDevicePermissions=None, QFileDevicePermission=None):
        'setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool\nsetPermissions(str, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool'
        return True
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def symLinkTarget(cls, self):
        'symLinkTarget(self) -> str\nsymLinkTarget(str) -> str'
        return ''
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def unmap(cls, self, sipvoidptr):
        'unmap(self, sip.voidptr) -> bool'
        return True
    
    @classmethod
    def unsetError(cls, self):
        'unsetError(self)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls):
        pass
    

class QFileDevice(QIODevice):
    AbortError = FileError()
    AutoCloseHandle = FileHandleFlag()
    CopyError = FileError()
    DontCloseHandle = FileHandleFlag()
    ExeGroup = Permission()
    ExeOther = Permission()
    ExeOwner = Permission()
    ExeUser = Permission()
    FatalError = FileError()
    FileError = FileError
    FileHandleFlag = FileHandleFlag
    FileHandleFlags = FileHandleFlags
    MapPrivateOption = MemoryMapFlags()
    MemoryMapFlags = MemoryMapFlags
    NoError = FileError()
    NoOptions = MemoryMapFlags()
    OpenError = FileError()
    Permission = Permission
    Permissions = Permissions
    PermissionsError = FileError()
    PositionError = FileError()
    ReadError = FileError()
    ReadGroup = Permission()
    ReadOther = Permission()
    ReadOwner = Permission()
    ReadUser = Permission()
    RemoveError = FileError()
    RenameError = FileError()
    ResizeError = FileError()
    ResourceError = FileError()
    TimeOutError = FileError()
    UnspecifiedError = FileError()
    WriteError = FileError()
    WriteGroup = Permission()
    WriteOther = Permission()
    WriteOwner = Permission()
    WriteUser = Permission()
    __class__ = QFileDevice
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QFileDevice.FileError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls, self):
        'flush(self) -> bool'
        return True
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def handle(cls, self):
        'handle(self) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def map(cls, self, int, int_, flags: QFileDevice.MemoryMapFlags=QFileDevice.NoOptions):
        'map(self, int, int, flags: QFileDevice.MemoryMapFlags = QFileDevice.NoOptions) -> sip.voidptr'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def permissions(cls, self):
        'permissions(self) -> QFileDevice.Permissions'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls, self, int):
        'readData(self, int) -> bytes'
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls, self, int):
        'readLineData(self, int) -> bytes'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setErrorString(cls, self, str):
        'setErrorString(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'setOpenMode(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag])'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPermissions(cls, self, UnionQFileDevicePermissions=None, QFileDevicePermission=None):
        'setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool'
        return True
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def unmap(cls, self, sipvoidptr):
        'unmap(self, sip.voidptr) -> bool'
        return True
    
    @classmethod
    def unsetError(cls, self):
        'unsetError(self)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls, self, bytes):
        'writeData(self, bytes) -> int'
        return 1
    

class QFileInfo(_mod_sip.simplewrapper):
    'QFileInfo()\nQFileInfo(str)\nQFileInfo(QFile)\nQFileInfo(QDir, str)\nQFileInfo(QFileInfo)'
    __class__ = QFileInfo
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    @classmethod
    def __fspath__(cls, self):
        '__fspath__(self) -> object'
        pass
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QFileInfo):
        'QFileInfo()\nQFileInfo(str)\nQFileInfo(QFile)\nQFileInfo(QDir, str)\nQFileInfo(QFileInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def absoluteDir(cls, self):
        'absoluteDir(self) -> QDir'
        pass
    
    @classmethod
    def absoluteFilePath(cls, self):
        'absoluteFilePath(self) -> str'
        return ''
    
    @classmethod
    def absolutePath(cls, self):
        'absolutePath(self) -> str'
        return ''
    
    @classmethod
    def baseName(cls, self):
        'baseName(self) -> str'
        return ''
    
    @classmethod
    def bundleName(cls, self):
        'bundleName(self) -> str'
        return ''
    
    @classmethod
    def caching(cls, self):
        'caching(self) -> bool'
        return True
    
    @classmethod
    def canonicalFilePath(cls, self):
        'canonicalFilePath(self) -> str'
        return ''
    
    @classmethod
    def canonicalPath(cls, self):
        'canonicalPath(self) -> str'
        return ''
    
    @classmethod
    def completeBaseName(cls, self):
        'completeBaseName(self) -> str'
        return ''
    
    @classmethod
    def completeSuffix(cls, self):
        'completeSuffix(self) -> str'
        return ''
    
    @classmethod
    def created(cls, self):
        'created(self) -> QDateTime'
        pass
    
    @classmethod
    def dir(cls, self):
        'dir(self) -> QDir'
        pass
    
    @classmethod
    def exists(cls, self):
        'exists(self) -> bool\nexists(str) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def filePath(cls, self):
        'filePath(self) -> str'
        return ''
    
    @classmethod
    def group(cls, self):
        'group(self) -> str'
        return ''
    
    @classmethod
    def groupId(cls, self):
        'groupId(self) -> int'
        return 1
    
    @classmethod
    def isAbsolute(cls, self):
        'isAbsolute(self) -> bool'
        return True
    
    @classmethod
    def isBundle(cls, self):
        'isBundle(self) -> bool'
        return True
    
    @classmethod
    def isDir(cls, self):
        'isDir(self) -> bool'
        return True
    
    @classmethod
    def isExecutable(cls, self):
        'isExecutable(self) -> bool'
        return True
    
    @classmethod
    def isFile(cls, self):
        'isFile(self) -> bool'
        return True
    
    @classmethod
    def isHidden(cls, self):
        'isHidden(self) -> bool'
        return True
    
    @classmethod
    def isNativePath(cls, self):
        'isNativePath(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isRelative(cls, self):
        'isRelative(self) -> bool'
        return True
    
    @classmethod
    def isRoot(cls, self):
        'isRoot(self) -> bool'
        return True
    
    @classmethod
    def isSymLink(cls, self):
        'isSymLink(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def lastModified(cls, self):
        'lastModified(self) -> QDateTime'
        pass
    
    @classmethod
    def lastRead(cls, self):
        'lastRead(self) -> QDateTime'
        pass
    
    @classmethod
    def makeAbsolute(cls, self):
        'makeAbsolute(self) -> bool'
        return True
    
    @classmethod
    def owner(cls, self):
        'owner(self) -> str'
        return ''
    
    @classmethod
    def ownerId(cls, self):
        'ownerId(self) -> int'
        return 1
    
    @classmethod
    def path(cls, self):
        'path(self) -> str'
        return ''
    
    @classmethod
    def permission(cls, self, UnionQFileDevicePermissions=None, QFileDevicePermission=None):
        'permission(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool'
        return True
    
    @classmethod
    def permissions(cls, self):
        'permissions(self) -> QFileDevice.Permissions'
        pass
    
    @classmethod
    def refresh(cls, self):
        'refresh(self)'
        pass
    
    @classmethod
    def setCaching(cls, self, bool):
        'setCaching(self, bool)'
        pass
    
    @classmethod
    def setFile(cls, self, QDir, str):
        'setFile(self, str)\nsetFile(self, QFile)\nsetFile(self, QDir, str)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def suffix(cls, self):
        'suffix(self) -> str'
        return ''
    
    @classmethod
    def swap(cls, self, QFileInfo):
        'swap(self, QFileInfo)'
        pass
    
    @classmethod
    def symLinkTarget(cls, self):
        'symLinkTarget(self) -> str'
        return ''
    

class QFileSelector(QObject):
    'QFileSelector(parent: QObject = None)'
    __class__ = QFileSelector
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QFileSelector(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def allSelectors(cls, self):
        'allSelectors(self) -> List[str]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def extraSelectors(cls, self):
        'extraSelectors(self) -> List[str]'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def select(cls, self, QUrl):
        'select(self, str) -> str\nselect(self, QUrl) -> QUrl'
        return ''
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setExtraSelectors(cls, self, Iterablestr=None):
        'setExtraSelectors(self, Iterable[str])'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QFileSystemWatcher(QObject):
    'QFileSystemWatcher(parent: QObject = None)\nQFileSystemWatcher(Iterable[str], parent: QObject = None)'
    __class__ = QFileSystemWatcher
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, Iterablestr=None, parent: QObject=None):
        'QFileSystemWatcher(parent: QObject = None)\nQFileSystemWatcher(Iterable[str], parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addPath(cls, self, str):
        'addPath(self, str) -> bool'
        return True
    
    @classmethod
    def addPaths(cls, self, Iterablestr=None):
        'addPaths(self, Iterable[str]) -> List[str]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def directories(cls, self):
        'directories(self) -> List[str]'
        pass
    
    def directoryChanged(self, str):
        'directoryChanged(self, str) [signal]'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    def fileChanged(self, str):
        'fileChanged(self, str) [signal]'
        pass
    
    @classmethod
    def files(cls, self):
        'files(self) -> List[str]'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removePath(cls, self, str):
        'removePath(self, str) -> bool'
        return True
    
    @classmethod
    def removePaths(cls, self, Iterablestr=None):
        'removePaths(self, Iterable[str]) -> List[str]'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QFinalState(QAbstractState):
    'QFinalState(parent: QState = None)'
    __class__ = QFinalState
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QState=None):
        'QFinalState(parent: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def active(cls, self):
        'active(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onEntry(cls, self, QEvent):
        'onEntry(self, QEvent)'
        pass
    
    @classmethod
    def onExit(cls, self, QEvent):
        'onExit(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentState(cls, self):
        'parentState(self) -> QState'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QGenericArgument(_mod_sip.simplewrapper):
    __class__ = QGenericArgument
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class QGenericReturnArgument(_mod_sip.simplewrapper):
    __class__ = QGenericReturnArgument
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class QHistoryState(QAbstractState):
    'QHistoryState(parent: QState = None)\nQHistoryState(QHistoryState.HistoryType, parent: QState = None)'
    DeepHistory = HistoryType()
    HistoryType = HistoryType
    ShallowHistory = HistoryType()
    __class__ = QHistoryState
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QHistoryStateHistoryType, parent: QState=None):
        'QHistoryState(parent: QState = None)\nQHistoryState(QHistoryState.HistoryType, parent: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def active(cls, self):
        'active(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def defaultState(cls, self):
        'defaultState(self) -> QAbstractState'
        pass
    
    def defaultStateChanged(self):
        'defaultStateChanged(self) [signal]'
        pass
    
    @classmethod
    def defaultTransition(cls, self):
        'defaultTransition(self) -> QAbstractTransition'
        pass
    
    def defaultTransitionChanged(self):
        'defaultTransitionChanged(self) [signal]'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def historyType(cls, self):
        'historyType(self) -> QHistoryState.HistoryType'
        pass
    
    def historyTypeChanged(self):
        'historyTypeChanged(self) [signal]'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onEntry(cls, self, QEvent):
        'onEntry(self, QEvent)'
        pass
    
    @classmethod
    def onExit(cls, self, QEvent):
        'onExit(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentState(cls, self):
        'parentState(self) -> QState'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setDefaultState(cls, self, QAbstractState):
        'setDefaultState(self, QAbstractState)'
        pass
    
    @classmethod
    def setDefaultTransition(cls, self, QAbstractTransition):
        'setDefaultTransition(self, QAbstractTransition)'
        pass
    
    @classmethod
    def setHistoryType(cls, self, QHistoryStateHistoryType):
        'setHistoryType(self, QHistoryState.HistoryType)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QIODevice(QObject):
    'QIODevice()\nQIODevice(QObject)'
    Append = OpenModeFlag()
    NotOpen = OpenModeFlag()
    OpenMode = OpenMode
    OpenModeFlag = OpenModeFlag
    ReadOnly = OpenModeFlag()
    ReadWrite = OpenModeFlag()
    Text = OpenModeFlag()
    Truncate = OpenModeFlag()
    Unbuffered = OpenModeFlag()
    WriteOnly = OpenModeFlag()
    __class__ = QIODevice
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QObject):
        'QIODevice()\nQIODevice(QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def aboutToClose(self):
        'aboutToClose(self) [signal]'
        pass
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    def bytesWritten(self, int):
        'bytesWritten(self, int) [signal]'
        pass
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    def channelBytesWritten(self, int, int_):
        'channelBytesWritten(self, int, int) [signal]'
        pass
    
    def channelReadyRead(self, int):
        'channelReadyRead(self, int) [signal]'
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    def readChannelFinished(self):
        'readChannelFinished(self) [signal]'
        pass
    
    @classmethod
    def readData(cls, self, int):
        'readData(self, int) -> bytes'
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls, self, int):
        'readLineData(self, int) -> bytes'
        pass
    
    def readyRead(self):
        'readyRead(self) [signal]'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setErrorString(cls, self, str):
        'setErrorString(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'setOpenMode(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag])'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls, self, bytes):
        'writeData(self, bytes) -> int'
        return 1
    

class QIdentityProxyModel(QAbstractProxyModel):
    'QIdentityProxyModel(parent: QObject = None)'
    __class__ = QIdentityProxyModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QIdentityProxyModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls, self, parent: QModelIndex=QModelIndex()):
        'columnCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls, self, parent: QModelIndex=QModelIndex()):
        'hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> Dict[int, Any]'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def mapFromSource(cls, self, QModelIndex):
        'mapFromSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def mapSelectionFromSource(cls, self, QItemSelection):
        'mapSelectionFromSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapSelectionToSource(cls, self, QItemSelection):
        'mapSelectionToSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapToSource(cls, self, QModelIndex):
        'mapToSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self, QModelIndex):
        'parent(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls):
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setSourceModel(cls, self, QAbstractItemModel):
        'setSourceModel(self, QAbstractItemModel)'
        pass
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def sourceModel(cls, self):
        'sourceModel(self) -> QAbstractItemModel'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QItemSelection(_mod_sip.simplewrapper):
    'QItemSelection()\nQItemSelection(QModelIndex, QModelIndex)\nQItemSelection(QItemSelection)'
    __class__ = QItemSelection
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Implement self+=value.'
        return None
    
    def __init__(self, QModelIndex, QModelIndex_):
        'QItemSelection()\nQItemSelection(QModelIndex, QModelIndex)\nQItemSelection(QItemSelection)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def append(cls, self, QItemSelectionRange):
        'append(self, QItemSelectionRange)'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def contains(cls, self, QModelIndex):
        'contains(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def count(cls, self, QItemSelectionRange):
        'count(self, QItemSelectionRange) -> int\ncount(self) -> int'
        return 1
    
    @classmethod
    def first(cls, self):
        'first(self) -> QItemSelectionRange'
        pass
    
    @classmethod
    def indexOf(cls, self, QItemSelectionRange, from_: int=0):
        'indexOf(self, QItemSelectionRange, from_: int = 0) -> int'
        return 1
    
    @classmethod
    def indexes(cls, self):
        'indexes(self) -> object'
        pass
    
    @classmethod
    def insert(cls, self, int, QItemSelectionRange):
        'insert(self, int, QItemSelectionRange)'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def last(cls, self):
        'last(self) -> QItemSelectionRange'
        pass
    
    @classmethod
    def lastIndexOf(cls, self, QItemSelectionRange, from_: int=-1):
        'lastIndexOf(self, QItemSelectionRange, from_: int = -1) -> int'
        return 1
    
    @classmethod
    def merge(cls, self, QItemSelection, UnionQItemSelectionModelSelectionFlags=None, QItemSelectionModelSelectionFlag=None):
        'merge(self, QItemSelection, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])'
        pass
    
    @classmethod
    def move(cls, self, int, int_):
        'move(self, int, int)'
        pass
    
    @classmethod
    def prepend(cls, self, QItemSelectionRange):
        'prepend(self, QItemSelectionRange)'
        pass
    
    @classmethod
    def removeAll(cls, self, QItemSelectionRange):
        'removeAll(self, QItemSelectionRange) -> int'
        return 1
    
    @classmethod
    def removeAt(cls, self, int):
        'removeAt(self, int)'
        pass
    
    @classmethod
    def replace(cls, self, int, QItemSelectionRange):
        'replace(self, int, QItemSelectionRange)'
        pass
    
    @classmethod
    def select(cls, self, QModelIndex, QModelIndex_):
        'select(self, QModelIndex, QModelIndex)'
        pass
    
    @classmethod
    def split(cls, QItemSelectionRange, QItemSelectionRange_, QItemSelection):
        'split(QItemSelectionRange, QItemSelectionRange, QItemSelection)'
        pass
    
    @classmethod
    def swap(cls, self, int, int_):
        'swap(self, int, int)'
        pass
    
    @classmethod
    def takeAt(cls, self, int):
        'takeAt(self, int) -> QItemSelectionRange'
        pass
    
    @classmethod
    def takeFirst(cls, self):
        'takeFirst(self) -> QItemSelectionRange'
        pass
    
    @classmethod
    def takeLast(cls, self):
        'takeLast(self) -> QItemSelectionRange'
        pass
    

class QItemSelectionModel(QObject):
    'QItemSelectionModel(model: QAbstractItemModel = None)\nQItemSelectionModel(QAbstractItemModel, QObject)'
    Clear = SelectionFlag()
    ClearAndSelect = SelectionFlag()
    Columns = SelectionFlag()
    Current = SelectionFlag()
    Deselect = SelectionFlag()
    NoUpdate = SelectionFlag()
    Rows = SelectionFlag()
    Select = SelectionFlag()
    SelectCurrent = SelectionFlag()
    SelectionFlag = SelectionFlag
    SelectionFlags = SelectionFlags
    Toggle = SelectionFlag()
    ToggleCurrent = SelectionFlag()
    __class__ = QItemSelectionModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, model: QAbstractItemModel=None):
        'QItemSelectionModel(model: QAbstractItemModel = None)\nQItemSelectionModel(QAbstractItemModel, QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def clearCurrentIndex(cls, self):
        'clearCurrentIndex(self)'
        pass
    
    @classmethod
    def clearSelection(cls, self):
        'clearSelection(self)'
        pass
    
    @classmethod
    def columnIntersectsSelection(cls, self, int, QModelIndex):
        'columnIntersectsSelection(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def connectNotify(cls):
        pass
    
    def currentChanged(self, QModelIndex, QModelIndex_):
        'currentChanged(self, QModelIndex, QModelIndex) [signal]'
        pass
    
    def currentColumnChanged(self, QModelIndex, QModelIndex_):
        'currentColumnChanged(self, QModelIndex, QModelIndex) [signal]'
        pass
    
    @classmethod
    def currentIndex(cls, self):
        'currentIndex(self) -> QModelIndex'
        pass
    
    def currentRowChanged(self, QModelIndex, QModelIndex_):
        'currentRowChanged(self, QModelIndex, QModelIndex) [signal]'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def emitSelectionChanged(cls, self, QItemSelection, QItemSelection_):
        'emitSelectionChanged(self, QItemSelection, QItemSelection)'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def hasSelection(cls, self):
        'hasSelection(self) -> bool'
        return True
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isColumnSelected(cls, self, int, QModelIndex):
        'isColumnSelected(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def isRowSelected(cls, self, int, QModelIndex):
        'isRowSelected(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def isSelected(cls, self, QModelIndex):
        'isSelected(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def model(cls, self):
        'model(self) -> QAbstractItemModel'
        pass
    
    def modelChanged(self, QAbstractItemModel):
        'modelChanged(self, QAbstractItemModel) [signal]'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self)'
        pass
    
    @classmethod
    def rowIntersectsSelection(cls, self, int, QModelIndex):
        'rowIntersectsSelection(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def select(cls, self, QItemSelection, UnionQItemSelectionModelSelectionFlags=None, QItemSelectionModelSelectionFlag=None):
        'select(self, QModelIndex, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])\nselect(self, QItemSelection, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])'
        pass
    
    @classmethod
    def selectedColumns(cls, self, row: int=0):
        'selectedColumns(self, row: int = 0) -> object'
        pass
    
    @classmethod
    def selectedIndexes(cls, self):
        'selectedIndexes(self) -> object'
        pass
    
    @classmethod
    def selectedRows(cls, self, column: int=0):
        'selectedRows(self, column: int = 0) -> object'
        pass
    
    @classmethod
    def selection(cls, self):
        'selection(self) -> QItemSelection'
        pass
    
    def selectionChanged(self, QItemSelection, QItemSelection_):
        'selectionChanged(self, QItemSelection, QItemSelection) [signal]'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentIndex(cls, self, QModelIndex, UnionQItemSelectionModelSelectionFlags=None, QItemSelectionModelSelectionFlag=None):
        'setCurrentIndex(self, QModelIndex, Union[QItemSelectionModel.SelectionFlags, QItemSelectionModel.SelectionFlag])'
        pass
    
    @classmethod
    def setModel(cls, self, QAbstractItemModel):
        'setModel(self, QAbstractItemModel)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QItemSelectionRange(_mod_sip.simplewrapper):
    'QItemSelectionRange()\nQItemSelectionRange(QItemSelectionRange)\nQItemSelectionRange(QModelIndex, QModelIndex)\nQItemSelectionRange(QModelIndex)'
    __class__ = QItemSelectionRange
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QModelIndex, QModelIndex_):
        'QItemSelectionRange()\nQItemSelectionRange(QItemSelectionRange)\nQItemSelectionRange(QModelIndex, QModelIndex)\nQItemSelectionRange(QModelIndex)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def bottom(cls, self):
        'bottom(self) -> int'
        return 1
    
    @classmethod
    def bottomRight(cls, self):
        'bottomRight(self) -> QPersistentModelIndex'
        pass
    
    @classmethod
    def contains(cls, self, int, int_, QModelIndex):
        'contains(self, QModelIndex) -> bool\ncontains(self, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def height(cls, self):
        'height(self) -> int'
        return 1
    
    @classmethod
    def indexes(cls, self):
        'indexes(self) -> object'
        pass
    
    @classmethod
    def intersected(cls, self, QItemSelectionRange):
        'intersected(self, QItemSelectionRange) -> QItemSelectionRange'
        pass
    
    @classmethod
    def intersects(cls, self, QItemSelectionRange):
        'intersects(self, QItemSelectionRange) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def left(cls, self):
        'left(self) -> int'
        return 1
    
    @classmethod
    def model(cls, self):
        'model(self) -> QAbstractItemModel'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QModelIndex'
        pass
    
    @classmethod
    def right(cls, self):
        'right(self) -> int'
        return 1
    
    @classmethod
    def swap(cls, self, QItemSelectionRange):
        'swap(self, QItemSelectionRange)'
        pass
    
    @classmethod
    def top(cls, self):
        'top(self) -> int'
        return 1
    
    @classmethod
    def topLeft(cls, self):
        'topLeft(self) -> QPersistentModelIndex'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> int'
        return 1
    

class QJsonDocument(_mod_sip.simplewrapper):
    'QJsonDocument()\nQJsonDocument(Dict[str, QJsonValue])\nQJsonDocument(Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]])\nQJsonDocument(QJsonDocument)'
    BypassValidation = DataValidation()
    Compact = JsonFormat()
    DataValidation = DataValidation
    Indented = JsonFormat()
    JsonFormat = JsonFormat
    Validate = DataValidation()
    __class__ = QJsonDocument
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, IterableUnionQJsonValue=None, QJsonValueType=None, Dictstr=None, QJsonValue=None, bool=None, int=None, float=None, str=None):
        'QJsonDocument()\nQJsonDocument(Dict[str, QJsonValue])\nQJsonDocument(Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]])\nQJsonDocument(QJsonDocument)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def array(cls, self):
        'array(self) -> List[QJsonValue]'
        pass
    
    @classmethod
    def fromBinaryData(cls, UnionQByteArray=None, bytes=None, bytearray=None, validation: QJsonDocument.DataValidation=QJsonDocument.Validate):
        'fromBinaryData(Union[QByteArray, bytes, bytearray], validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument'
        pass
    
    @classmethod
    def fromJson(cls, UnionQByteArray=None, bytes=None, bytearray=None, error: QJsonParseError=None):
        'fromJson(Union[QByteArray, bytes, bytearray], error: QJsonParseError = None) -> QJsonDocument'
        pass
    
    @classmethod
    def fromRawData(cls, str, int, validation: QJsonDocument.DataValidation=QJsonDocument.Validate):
        'fromRawData(str, int, validation: QJsonDocument.DataValidation = QJsonDocument.Validate) -> QJsonDocument'
        pass
    
    @classmethod
    def fromVariant(cls, Any):
        'fromVariant(Any) -> QJsonDocument'
        pass
    
    @classmethod
    def isArray(cls, self):
        'isArray(self) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isObject(cls, self):
        'isObject(self) -> bool'
        return True
    
    @classmethod
    def object(cls, self):
        'object(self) -> Dict[str, QJsonValue]'
        pass
    
    @classmethod
    def rawData(cls, self):
        'rawData(self) -> Tuple[str, int]'
        pass
    
    @classmethod
    def setArray(cls, self, IterableUnionQJsonValue=None, QJsonValueType=None, Dictstr=None, QJsonValue=None, bool=None, int=None, float=None, str=None):
        'setArray(self, Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]])'
        pass
    
    @classmethod
    def setObject(cls, self, Dictstr=None, QJsonValue=None):
        'setObject(self, Dict[str, QJsonValue])'
        pass
    
    @classmethod
    def toBinaryData(cls, self):
        'toBinaryData(self) -> QByteArray'
        pass
    
    @classmethod
    def toJson(cls, self, QJsonDocumentJsonFormat):
        'toJson(self) -> QByteArray\ntoJson(self, QJsonDocument.JsonFormat) -> QByteArray'
        pass
    
    @classmethod
    def toVariant(cls, self):
        'toVariant(self) -> Any'
        pass
    

class QJsonParseError(_mod_sip.simplewrapper):
    'QJsonParseError()\nQJsonParseError(QJsonParseError)'
    DeepNesting = ParseError()
    DocumentTooLarge = ParseError()
    GarbageAtEnd = ParseError()
    IllegalEscapeSequence = ParseError()
    IllegalNumber = ParseError()
    IllegalUTF8String = ParseError()
    IllegalValue = ParseError()
    MissingNameSeparator = ParseError()
    MissingObject = ParseError()
    MissingValueSeparator = ParseError()
    NoError = ParseError()
    ParseError = ParseError
    TerminationByNumber = ParseError()
    UnterminatedArray = ParseError()
    UnterminatedObject = ParseError()
    UnterminatedString = ParseError()
    __class__ = QJsonParseError
    __dict__ = {}
    def __init__(self, QJsonParseError):
        'QJsonParseError()\nQJsonParseError(QJsonParseError)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    

class QJsonValue(_mod_sip.simplewrapper):
    'QJsonValue(type: QJsonValue.Type = QJsonValue.Null)\nQJsonValue(Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str])'
    Array = Type()
    Bool = Type()
    Double = Type()
    Null = Type()
    Object = Type()
    String = Type()
    Type = Type
    Undefined = Type()
    __class__ = QJsonValue
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, UnionQJsonValue=None, QJsonValueType=None, Dictstr=None, QJsonValue=None, bool=None, int=None, float=None, str=None):
        'QJsonValue(type: QJsonValue.Type = QJsonValue.Null)\nQJsonValue(Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def fromVariant(cls, Any):
        'fromVariant(Any) -> QJsonValue'
        pass
    
    @classmethod
    def isArray(cls, self):
        'isArray(self) -> bool'
        return True
    
    @classmethod
    def isBool(cls, self):
        'isBool(self) -> bool'
        return True
    
    @classmethod
    def isDouble(cls, self):
        'isDouble(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isObject(cls, self):
        'isObject(self) -> bool'
        return True
    
    @classmethod
    def isString(cls, self):
        'isString(self) -> bool'
        return True
    
    @classmethod
    def isUndefined(cls, self):
        'isUndefined(self) -> bool'
        return True
    
    @classmethod
    def toArray(cls, self, IterableUnionQJsonValue=None, QJsonValueType=None, Dictstr=None, QJsonValue=None, bool=None, int=None, float=None, str=None):
        'toArray(self) -> List[QJsonValue]\ntoArray(self, Iterable[Union[QJsonValue, QJsonValue.Type, Dict[str, QJsonValue], bool, int, float, str]]) -> List[QJsonValue]'
        pass
    
    @classmethod
    def toBool(cls, self, defaultValue: bool=False):
        'toBool(self, defaultValue: bool = False) -> bool'
        return True
    
    @classmethod
    def toDouble(cls, self, defaultValue: float=0):
        'toDouble(self, defaultValue: float = 0) -> float'
        return 1.0
    
    @classmethod
    def toInt(cls, self, defaultValue: int=0):
        'toInt(self, defaultValue: int = 0) -> int'
        return 1
    
    @classmethod
    def toObject(cls, self, Dictstr=None, QJsonValue=None):
        'toObject(self) -> Dict[str, QJsonValue]\ntoObject(self, Dict[str, QJsonValue]) -> Dict[str, QJsonValue]'
        pass
    
    @classmethod
    def toString(cls, self, str):
        'toString(self) -> str\ntoString(self, str) -> str'
        return ''
    
    @classmethod
    def toVariant(cls, self):
        'toVariant(self) -> Any'
        pass
    
    @classmethod
    def type(cls, self):
        'type(self) -> QJsonValue.Type'
        pass
    

class QLibrary(QObject):
    'QLibrary(parent: QObject = None)\nQLibrary(str, parent: QObject = None)\nQLibrary(str, int, parent: QObject = None)\nQLibrary(str, str, parent: QObject = None)'
    DeepBindHint = LoadHint()
    ExportExternalSymbolsHint = LoadHint()
    LoadArchiveMemberHint = LoadHint()
    LoadHint = LoadHint
    LoadHints = LoadHints
    PreventUnloadHint = LoadHint()
    ResolveAllSymbolsHint = LoadHint()
    __class__ = QLibrary
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, str_, parent: QObject=None):
        'QLibrary(parent: QObject = None)\nQLibrary(str, parent: QObject = None)\nQLibrary(str, int, parent: QObject = None)\nQLibrary(str, str, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isLibrary(cls, str):
        'isLibrary(str) -> bool'
        return True
    
    @classmethod
    def isLoaded(cls, self):
        'isLoaded(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def load(cls, self):
        'load(self) -> bool'
        return True
    
    @classmethod
    def loadHints(cls, self):
        'loadHints(self) -> QLibrary.LoadHints'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resolve(cls, str, str_, str_1):
        'resolve(self, str) -> sip.voidptr\nresolve(str, str) -> sip.voidptr\nresolve(str, int, str) -> sip.voidptr\nresolve(str, str, str) -> sip.voidptr'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setFileNameAndVersion(cls, self, str, str_):
        'setFileNameAndVersion(self, str, int)\nsetFileNameAndVersion(self, str, str)'
        pass
    
    @classmethod
    def setLoadHints(cls, self, UnionQLibraryLoadHints=None, QLibraryLoadHint=None):
        'setLoadHints(self, Union[QLibrary.LoadHints, QLibrary.LoadHint])'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def unload(cls, self):
        'unload(self) -> bool'
        return True
    

class QLibraryInfo(_mod_sip.simplewrapper):
    'QLibraryInfo(QLibraryInfo)'
    ArchDataPath = LibraryLocation()
    BinariesPath = LibraryLocation()
    DataPath = LibraryLocation()
    DocumentationPath = LibraryLocation()
    ExamplesPath = LibraryLocation()
    HeadersPath = LibraryLocation()
    ImportsPath = LibraryLocation()
    LibrariesPath = LibraryLocation()
    LibraryExecutablesPath = LibraryLocation()
    LibraryLocation = LibraryLocation
    PluginsPath = LibraryLocation()
    PrefixPath = LibraryLocation()
    Qml2ImportsPath = LibraryLocation()
    SettingsPath = LibraryLocation()
    TestsPath = LibraryLocation()
    TranslationsPath = LibraryLocation()
    __class__ = QLibraryInfo
    __dict__ = {}
    def __init__(self, QLibraryInfo):
        'QLibraryInfo(QLibraryInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def buildDate(cls):
        'buildDate() -> QDate'
        pass
    
    @classmethod
    def isDebugBuild(cls):
        'isDebugBuild() -> bool'
        return True
    
    @classmethod
    def licensedProducts(cls):
        'licensedProducts() -> str'
        return ''
    
    @classmethod
    def licensee(cls):
        'licensee() -> str'
        return ''
    
    @classmethod
    def location(cls, QLibraryInfoLibraryLocation):
        'location(QLibraryInfo.LibraryLocation) -> str'
        return ''
    
    @classmethod
    def version(cls):
        'version() -> QVersionNumber'
        pass
    

class QLine(_mod_sip.simplewrapper):
    'QLine()\nQLine(QPoint, QPoint)\nQLine(int, int, int, int)\nQLine(QLine)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QLine
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, int, int_, int_1, int_2):
        'QLine()\nQLine(QPoint, QPoint)\nQLine(int, int, int, int)\nQLine(QLine)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def center(cls, self):
        'center(self) -> QPoint'
        pass
    
    @classmethod
    def dx(cls, self):
        'dx(self) -> int'
        return 1
    
    @classmethod
    def dy(cls, self):
        'dy(self) -> int'
        return 1
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def p1(cls, self):
        'p1(self) -> QPoint'
        pass
    
    @classmethod
    def p2(cls, self):
        'p2(self) -> QPoint'
        pass
    
    @classmethod
    def setLine(cls, self, int, int_, int_1, int_2):
        'setLine(self, int, int, int, int)'
        pass
    
    @classmethod
    def setP1(cls, self, QPoint):
        'setP1(self, QPoint)'
        pass
    
    @classmethod
    def setP2(cls, self, QPoint):
        'setP2(self, QPoint)'
        pass
    
    @classmethod
    def setPoints(cls, self, QPoint, QPoint_):
        'setPoints(self, QPoint, QPoint)'
        pass
    
    @classmethod
    def translate(cls, self, int, int_):
        'translate(self, QPoint)\ntranslate(self, int, int)'
        pass
    
    @classmethod
    def translated(cls, self, int, int_):
        'translated(self, QPoint) -> QLine\ntranslated(self, int, int) -> QLine'
        pass
    
    @classmethod
    def x1(cls, self):
        'x1(self) -> int'
        return 1
    
    @classmethod
    def x2(cls, self):
        'x2(self) -> int'
        return 1
    
    @classmethod
    def y1(cls, self):
        'y1(self) -> int'
        return 1
    
    @classmethod
    def y2(cls, self):
        'y2(self) -> int'
        return 1
    

class QLineF(_mod_sip.simplewrapper):
    'QLineF(QLine)\nQLineF()\nQLineF(Union[QPointF, QPoint], Union[QPointF, QPoint])\nQLineF(float, float, float, float)\nQLineF(QLineF)'
    BoundedIntersection = IntersectType()
    IntersectType = IntersectType
    NoIntersection = IntersectType()
    UnboundedIntersection = IntersectType()
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QLineF
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, UnionQPointF=None, QPoint=None, UnionQPointF_=None, QPoint_=None):
        'QLineF(QLine)\nQLineF()\nQLineF(Union[QPointF, QPoint], Union[QPointF, QPoint])\nQLineF(float, float, float, float)\nQLineF(QLineF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def angle(cls, self):
        'angle(self) -> float'
        return 1.0
    
    @classmethod
    def angleTo(cls, self, QLineF):
        'angleTo(self, QLineF) -> float'
        return 1.0
    
    @classmethod
    def center(cls, self):
        'center(self) -> QPointF'
        pass
    
    @classmethod
    def dx(cls, self):
        'dx(self) -> float'
        return 1.0
    
    @classmethod
    def dy(cls, self):
        'dy(self) -> float'
        return 1.0
    
    @classmethod
    def fromPolar(cls, float, float_):
        'fromPolar(float, float) -> QLineF'
        pass
    
    @classmethod
    def intersect(cls, self, QLineF, UnionQPointF=None, QPoint=None):
        'intersect(self, QLineF, Union[QPointF, QPoint]) -> QLineF.IntersectType'
        pass
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def length(cls, self):
        'length(self) -> float'
        return 1.0
    
    @classmethod
    def normalVector(cls, self):
        'normalVector(self) -> QLineF'
        pass
    
    @classmethod
    def p1(cls, self):
        'p1(self) -> QPointF'
        pass
    
    @classmethod
    def p2(cls, self):
        'p2(self) -> QPointF'
        pass
    
    @classmethod
    def pointAt(cls, self, float):
        'pointAt(self, float) -> QPointF'
        pass
    
    @classmethod
    def setAngle(cls, self, float):
        'setAngle(self, float)'
        pass
    
    @classmethod
    def setLength(cls, self, float):
        'setLength(self, float)'
        pass
    
    @classmethod
    def setLine(cls, self, float, float_, float_1, float_2):
        'setLine(self, float, float, float, float)'
        pass
    
    @classmethod
    def setP1(cls, self, UnionQPointF=None, QPoint=None):
        'setP1(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setP2(cls, self, UnionQPointF=None, QPoint=None):
        'setP2(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setPoints(cls, self, UnionQPointF=None, QPoint=None, UnionQPointF_=None, QPoint_=None):
        'setPoints(self, Union[QPointF, QPoint], Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def toLine(cls, self):
        'toLine(self) -> QLine'
        pass
    
    @classmethod
    def translate(cls, self, UnionQPointF=None, QPoint=None):
        'translate(self, Union[QPointF, QPoint])\ntranslate(self, float, float)'
        pass
    
    @classmethod
    def translated(cls, self, UnionQPointF=None, QPoint=None):
        'translated(self, Union[QPointF, QPoint]) -> QLineF\ntranslated(self, float, float) -> QLineF'
        pass
    
    @classmethod
    def unitVector(cls, self):
        'unitVector(self) -> QLineF'
        pass
    
    @classmethod
    def x1(cls, self):
        'x1(self) -> float'
        return 1.0
    
    @classmethod
    def x2(cls, self):
        'x2(self) -> float'
        return 1.0
    
    @classmethod
    def y1(cls, self):
        'y1(self) -> float'
        return 1.0
    
    @classmethod
    def y2(cls, self):
        'y2(self) -> float'
        return 1.0
    

class QLocale(_mod_sip.simplewrapper):
    'QLocale()\nQLocale(str)\nQLocale(QLocale.Language, country: QLocale.Country = QLocale.AnyCountry)\nQLocale(QLocale)\nQLocale(QLocale.Language, QLocale.Script, QLocale.Country)'
    Abkhazian = Language()
    AdlamScript = Script()
    Afan = Language()
    Afar = Language()
    Afghanistan = Country()
    Afrikaans = Language()
    Aghem = Language()
    Ahom = Language()
    AhomScript = Script()
    Akan = Language()
    Akkadian = Language()
    Akoose = Language()
    AlandIslands = Country()
    Albania = Country()
    Albanian = Language()
    Algeria = Country()
    AlternateQuotation = QuotationStyle()
    AmericanSamoa = Country()
    AmericanSignLanguage = Language()
    Amharic = Language()
    AnatolianHieroglyphsScript = Script()
    AncientEgyptian = Language()
    AncientGreek = Language()
    AncientNorthArabian = Language()
    Andorra = Country()
    Angola = Country()
    Anguilla = Country()
    Antarctica = Country()
    AntiguaAndBarbuda = Country()
    AnyCountry = Country()
    AnyLanguage = Language()
    AnyScript = Script()
    Arabic = Language()
    ArabicScript = Script()
    Aragonese = Language()
    Aramaic = Language()
    ArdhamagadhiPrakrit = Language()
    Argentina = Country()
    Armenia = Country()
    Armenian = Language()
    ArmenianScript = Script()
    Aruba = Country()
    AscensionIsland = Country()
    Assamese = Language()
    Asturian = Language()
    Asu = Language()
    Atsam = Language()
    Australia = Country()
    Austria = Country()
    Avaric = Language()
    Avestan = Language()
    AvestanScript = Script()
    Aymara = Language()
    Azerbaijan = Country()
    Azerbaijani = Language()
    Bafia = Language()
    Bahamas = Country()
    Bahrain = Country()
    Balinese = Language()
    BalineseScript = Script()
    Bambara = Language()
    BamumScript = Script()
    Bamun = Language()
    Bangladesh = Country()
    Barbados = Country()
    Basaa = Language()
    Bashkir = Language()
    Basque = Language()
    Bassa = Language()
    BassaVahScript = Script()
    BatakScript = Script()
    BatakToba = Language()
    Belarus = Country()
    Belarusian = Language()
    Belgium = Country()
    Belize = Country()
    Bemba = Language()
    Bena = Language()
    Bengali = Language()
    BengaliScript = Script()
    Benin = Country()
    Bermuda = Country()
    BhaiksukiScript = Script()
    Bhojpuri = Language()
    Bhutan = Country()
    Bhutani = Language()
    Bihari = Language()
    Bislama = Language()
    Blin = Language()
    Bodo = Language()
    Bolivia = Country()
    Bonaire = Country()
    BopomofoScript = Script()
    BosniaAndHerzegowina = Country()
    Bosnian = Language()
    Botswana = Country()
    BouvetIsland = Country()
    BrahmiScript = Script()
    BrailleScript = Script()
    Brazil = Country()
    Breton = Language()
    BritishIndianOceanTerritory = Country()
    BritishVirginIslands = Country()
    Brunei = Country()
    Buginese = Language()
    BugineseScript = Script()
    Buhid = Language()
    BuhidScript = Script()
    Bulgaria = Country()
    Bulgarian = Language()
    BurkinaFaso = Country()
    Burmese = Language()
    Burundi = Country()
    Byelorussian = Language()
    C = Language()
    Cambodia = Country()
    Cambodian = Language()
    Cameroon = Country()
    Canada = Country()
    CanadianAboriginalScript = Script()
    CanaryIslands = Country()
    Cantonese = Language()
    CapeVerde = Country()
    Carian = Language()
    CarianScript = Script()
    Catalan = Language()
    CaucasianAlbanianScript = Script()
    CaymanIslands = Country()
    CentralAfricanRepublic = Country()
    CentralKurdish = Language()
    CentralMoroccoTamazight = Language()
    CeutaAndMelilla = Country()
    Chad = Country()
    Chakma = Language()
    ChakmaScript = Script()
    ChamScript = Script()
    Chamorro = Language()
    Chechen = Language()
    Cherokee = Language()
    CherokeeScript = Script()
    Chewa = Language()
    Chiga = Language()
    Chile = Country()
    China = Country()
    Chinese = Language()
    ChristmasIsland = Country()
    Church = Language()
    Chuvash = Language()
    ClassicalMandaic = Language()
    ClippertonIsland = Country()
    CocosIslands = Country()
    Colognian = Language()
    Colombia = Country()
    Comoros = Country()
    CongoBrazzaville = Country()
    CongoKinshasa = Country()
    CongoSwahili = Language()
    CookIslands = Country()
    Coptic = Language()
    CopticScript = Script()
    Cornish = Language()
    Corsican = Language()
    CostaRica = Country()
    Country = Country
    Cree = Language()
    Croatia = Country()
    Croatian = Language()
    Cuba = Country()
    CuneiformScript = Script()
    CuraSao = Country()
    CurrencyDisplayName = CurrencySymbolFormat()
    CurrencyIsoCode = CurrencySymbolFormat()
    CurrencySymbol = CurrencySymbolFormat()
    CurrencySymbolFormat = CurrencySymbolFormat
    CypriotScript = Script()
    Cyprus = Country()
    CyrillicScript = Script()
    Czech = Language()
    CzechRepublic = Country()
    Danish = Language()
    DefaultNumberOptions = NumberOption()
    DemocraticRepublicOfCongo = Country()
    DemocraticRepublicOfKorea = Country()
    Denmark = Country()
    DeseretScript = Script()
    DevanagariScript = Script()
    DiegoGarcia = Country()
    Divehi = Language()
    Djibouti = Country()
    Dogri = Language()
    Dominica = Country()
    DominicanRepublic = Country()
    Duala = Language()
    DuployanScript = Script()
    Dutch = Language()
    Dzongkha = Language()
    EastTimor = Country()
    EasternCham = Language()
    EasternKayah = Language()
    Ecuador = Country()
    Egypt = Country()
    EgyptianHieroglyphsScript = Script()
    ElSalvador = Country()
    ElbasanScript = Script()
    Embu = Language()
    English = Language()
    EquatorialGuinea = Country()
    Eritrea = Country()
    Esperanto = Language()
    Estonia = Country()
    Estonian = Language()
    Ethiopia = Country()
    EthiopicScript = Script()
    Etruscan = Language()
    EuropeanUnion = Country()
    Ewe = Language()
    Ewondo = Language()
    FalklandIslands = Country()
    FaroeIslands = Country()
    Faroese = Language()
    Fiji = Country()
    Fijian = Language()
    Filipino = Language()
    Finland = Country()
    Finnish = Language()
    FloatingPointPrecisionOption = FloatingPointPrecisionOption
    FloatingPointShortest = FloatingPointPrecisionOption()
    FormatType = FormatType
    France = Country()
    FraserScript = Script()
    French = Language()
    FrenchGuiana = Country()
    FrenchPolynesia = Country()
    FrenchSouthernTerritories = Country()
    Frisian = Language()
    Friulian = Language()
    Fulah = Language()
    Ga = Language()
    Gabon = Country()
    Gaelic = Language()
    Galician = Language()
    Gambia = Country()
    Ganda = Language()
    Geez = Language()
    Georgia = Country()
    Georgian = Language()
    GeorgianScript = Script()
    German = Language()
    Germany = Country()
    Ghana = Country()
    Gibraltar = Country()
    GlagoliticScript = Script()
    Gothic = Language()
    GothicScript = Script()
    GranthaScript = Script()
    Greece = Country()
    Greek = Language()
    GreekScript = Script()
    Greenland = Country()
    Greenlandic = Language()
    Grenada = Country()
    Guadeloupe = Country()
    Guam = Country()
    Guarani = Language()
    Guatemala = Country()
    Guernsey = Country()
    Guinea = Country()
    GuineaBissau = Country()
    Gujarati = Language()
    GujaratiScript = Script()
    GurmukhiScript = Script()
    Gusii = Language()
    Guyana = Country()
    Haiti = Country()
    Haitian = Language()
    HanScript = Script()
    HanWithBopomofoScript = Script()
    HangulScript = Script()
    Hanunoo = Language()
    HanunooScript = Script()
    HatranScript = Script()
    Hausa = Language()
    Hawaiian = Language()
    HeardAndMcDonaldIslands = Country()
    Hebrew = Language()
    HebrewScript = Script()
    Herero = Language()
    HieroglyphicLuwian = Language()
    Hindi = Language()
    HiraganaScript = Script()
    HiriMotu = Language()
    HmongNjua = Language()
    Ho = Language()
    Honduras = Country()
    HongKong = Country()
    Hungarian = Language()
    Hungary = Country()
    Iceland = Country()
    Icelandic = Language()
    Igbo = Language()
    ImperialAramaicScript = Script()
    ImperialSystem = MeasurementSystem()
    ImperialUKSystem = MeasurementSystem()
    ImperialUSSystem = MeasurementSystem()
    InariSami = Language()
    IncludeTrailingZeroesAfterDot = NumberOption()
    India = Country()
    Indonesia = Country()
    Indonesian = Language()
    Ingush = Language()
    InscriptionalPahlaviScript = Script()
    InscriptionalParthianScript = Script()
    Interlingua = Language()
    Interlingue = Language()
    Inuktitut = Language()
    Inupiak = Language()
    Iran = Country()
    Iraq = Country()
    Ireland = Country()
    Irish = Language()
    IsleOfMan = Country()
    Israel = Country()
    Italian = Language()
    Italy = Country()
    IvoryCoast = Country()
    Jamaica = Country()
    JamoScript = Script()
    Japan = Country()
    Japanese = Language()
    JapaneseScript = Script()
    Javanese = Language()
    JavaneseScript = Script()
    Jersey = Country()
    Jju = Language()
    JolaFonyi = Language()
    Jordan = Country()
    Kabuverdianu = Language()
    Kabyle = Language()
    KaithiScript = Script()
    Kako = Language()
    Kalenjin = Language()
    Kamba = Language()
    Kannada = Language()
    KannadaScript = Script()
    Kanuri = Language()
    Kashmiri = Language()
    KatakanaScript = Script()
    KayahLiScript = Script()
    Kazakh = Language()
    Kazakhstan = Country()
    Kenya = Country()
    Kenyang = Language()
    KharoshthiScript = Script()
    Khmer = Language()
    KhmerScript = Script()
    KhojkiScript = Script()
    KhudawadiScript = Script()
    Kiche = Language()
    Kikuyu = Language()
    Kinyarwanda = Language()
    Kirghiz = Language()
    Kiribati = Country()
    Komi = Language()
    Kongo = Language()
    Konkani = Language()
    Korean = Language()
    KoreanScript = Script()
    Koro = Language()
    Kosovo = Country()
    KoyraChiini = Language()
    KoyraboroSenni = Language()
    Kpelle = Language()
    Kurdish = Language()
    Kurundi = Language()
    Kuwait = Country()
    Kwanyama = Language()
    Kwasio = Language()
    Kyrgyzstan = Country()
    Lakota = Language()
    Langi = Language()
    Language = Language
    LannaScript = Script()
    Lao = Language()
    LaoScript = Script()
    Laos = Country()
    LargeFloweryMiao = Language()
    LastCountry = Country()
    LastLanguage = Language()
    Latin = Language()
    LatinAmericaAndTheCaribbean = Country()
    LatinScript = Script()
    Latvia = Country()
    Latvian = Language()
    Lebanon = Country()
    Lepcha = Language()
    LepchaScript = Script()
    Lesotho = Country()
    Lezghian = Language()
    Liberia = Country()
    Libya = Country()
    Liechtenstein = Country()
    Limbu = Language()
    LimbuScript = Script()
    Limburgish = Language()
    LinearA = Language()
    LinearAScript = Script()
    LinearBScript = Script()
    Lingala = Language()
    Lisu = Language()
    LiteraryChinese = Language()
    Lithuania = Country()
    Lithuanian = Language()
    LongFormat = FormatType()
    LowGerman = Language()
    LowerSorbian = Language()
    Lu = Language()
    LubaKatanga = Language()
    LuleSami = Language()
    Luo = Language()
    Luxembourg = Country()
    Luxembourgish = Language()
    Luyia = Language()
    Lycian = Language()
    LycianScript = Script()
    Lydian = Language()
    LydianScript = Script()
    Macau = Country()
    Macedonia = Country()
    Macedonian = Language()
    Machame = Language()
    Madagascar = Country()
    MahajaniScript = Script()
    Maithili = Language()
    MakhuwaMeetto = Language()
    Makonde = Language()
    Malagasy = Language()
    Malawi = Country()
    Malay = Language()
    Malayalam = Language()
    MalayalamScript = Script()
    Malaysia = Country()
    Maldives = Country()
    Mali = Country()
    Malta = Country()
    Maltese = Language()
    MandaeanScript = Script()
    Mandingo = Language()
    ManichaeanMiddlePersian = Language()
    ManichaeanScript = Script()
    Manipuri = Language()
    Manx = Language()
    Maori = Language()
    Mapuche = Language()
    Marathi = Language()
    MarchenScript = Script()
    MarshallIslands = Country()
    Marshallese = Language()
    Martinique = Country()
    Masai = Language()
    Mauritania = Country()
    Mauritius = Country()
    Mayotte = Country()
    Mazanderani = Language()
    MeasurementSystem = MeasurementSystem
    MeiteiMayekScript = Script()
    Mende = Language()
    MendeKikakuiScript = Script()
    Meroitic = Language()
    MeroiticCursiveScript = Script()
    MeroiticScript = Script()
    Meru = Language()
    Meta = Language()
    MetricSystem = MeasurementSystem()
    Mexico = Country()
    Micronesia = Country()
    ModiScript = Script()
    Mohawk = Language()
    Moldavian = Language()
    Moldova = Country()
    Monaco = Country()
    Mongolia = Country()
    Mongolian = Language()
    MongolianScript = Script()
    Mono = Language()
    Montenegro = Country()
    Montserrat = Country()
    Morisyen = Language()
    Morocco = Country()
    Mozambique = Country()
    MroScript = Script()
    Mru = Language()
    MultaniScript = Script()
    Mundang = Language()
    Myanmar = Country()
    MyanmarScript = Script()
    NabataeanScript = Script()
    Nama = Language()
    Namibia = Country()
    NarrowFormat = FormatType()
    NauruCountry = Country()
    NauruLanguage = Language()
    Navaho = Language()
    Ndonga = Language()
    Nepal = Country()
    Nepali = Language()
    Netherlands = Country()
    NewCaledonia = Country()
    NewTaiLueScript = Script()
    NewZealand = Country()
    NewaScript = Script()
    Newari = Language()
    Ngiemboon = Language()
    Ngomba = Language()
    Nicaragua = Country()
    Niger = Country()
    Nigeria = Country()
    Niue = Country()
    Nko = Language()
    NkoScript = Script()
    NorfolkIsland = Country()
    NorthKorea = Country()
    NorthNdebele = Language()
    NorthernLuri = Language()
    NorthernMarianaIslands = Country()
    NorthernSami = Language()
    NorthernSotho = Language()
    NorthernThai = Language()
    Norway = Country()
    Norwegian = Language()
    NorwegianBokmal = Language()
    NorwegianNynorsk = Language()
    Nuer = Language()
    NumberOption = NumberOption
    NumberOptions = NumberOptions
    Nyanja = Language()
    Nyankole = Language()
    Occitan = Language()
    OghamScript = Script()
    Ojibwa = Language()
    OlChikiScript = Script()
    OldHungarianScript = Script()
    OldIrish = Language()
    OldItalicScript = Script()
    OldNorse = Language()
    OldNorthArabianScript = Script()
    OldPermicScript = Script()
    OldPersian = Language()
    OldPersianScript = Script()
    OldSouthArabianScript = Script()
    OldTurkish = Language()
    Oman = Country()
    OmitGroupSeparator = NumberOption()
    OmitLeadingZeroInExponent = NumberOption()
    Oriya = Language()
    OriyaScript = Script()
    OrkhonScript = Script()
    Oromo = Language()
    Osage = Language()
    OsageScript = Script()
    OsmanyaScript = Script()
    Ossetic = Language()
    OutlyingOceania = Country()
    PahawhHmongScript = Script()
    Pahlavi = Language()
    Pakistan = Country()
    Palau = Country()
    Palauan = Language()
    PalestinianTerritories = Country()
    Pali = Language()
    PalmyreneScript = Script()
    Panama = Country()
    Papiamento = Language()
    PapuaNewGuinea = Country()
    Paraguay = Country()
    Parthian = Language()
    Pashto = Language()
    PauCinHauScript = Script()
    PeoplesRepublicOfCongo = Country()
    Persian = Language()
    Peru = Country()
    PhagsPaScript = Script()
    Philippines = Country()
    Phoenician = Language()
    PhoenicianScript = Script()
    Pitcairn = Country()
    Poland = Country()
    Polish = Language()
    PollardPhoneticScript = Script()
    Portugal = Country()
    Portuguese = Language()
    PrakritLanguage = Language()
    Prussian = Language()
    PsalterPahlaviScript = Script()
    PuertoRico = Country()
    Punjabi = Language()
    Qatar = Country()
    Quechua = Language()
    QuotationStyle = QuotationStyle
    Rejang = Language()
    RejangScript = Script()
    RejectGroupSeparator = NumberOption()
    RejectLeadingZeroInExponent = NumberOption()
    RejectTrailingZeroesAfterDot = NumberOption()
    RepublicOfKorea = Country()
    Reunion = Country()
    RhaetoRomance = Language()
    Romania = Country()
    Romanian = Language()
    Romansh = Language()
    Rombo = Language()
    Rundi = Language()
    RunicScript = Script()
    Russia = Country()
    Russian = Language()
    RussianFederation = Country()
    Rwa = Language()
    Rwanda = Country()
    Sabaean = Language()
    Saho = Language()
    SaintBarthelemy = Country()
    SaintHelena = Country()
    SaintKittsAndNevis = Country()
    SaintLucia = Country()
    SaintMartin = Country()
    SaintPierreAndMiquelon = Country()
    SaintVincentAndTheGrenadines = Country()
    Sakha = Language()
    Samaritan = Language()
    SamaritanScript = Script()
    Samburu = Language()
    Samoa = Country()
    Samoan = Language()
    SanMarino = Country()
    Sango = Language()
    Sangu = Language()
    Sanskrit = Language()
    Santali = Language()
    SaoTomeAndPrincipe = Country()
    Saraiki = Language()
    Sardinian = Language()
    SaudiArabia = Country()
    Saurashtra = Language()
    SaurashtraScript = Script()
    Script = Script
    Sena = Language()
    Senegal = Country()
    Serbia = Country()
    Serbian = Language()
    SerboCroatian = Language()
    Seychelles = Country()
    Shambala = Language()
    SharadaScript = Script()
    ShavianScript = Script()
    Shona = Language()
    ShortFormat = FormatType()
    SichuanYi = Language()
    Sidamo = Language()
    SiddhamScript = Script()
    SierraLeone = Country()
    SignWritingScript = Script()
    SimplifiedChineseScript = Script()
    SimplifiedHanScript = Script()
    Sindhi = Language()
    Singapore = Country()
    Sinhala = Language()
    SinhalaScript = Script()
    SintMaarten = Country()
    SkoltSami = Language()
    Slovak = Language()
    Slovakia = Country()
    Slovenia = Country()
    Slovenian = Language()
    Soga = Language()
    SolomonIslands = Country()
    Somali = Language()
    Somalia = Country()
    Sora = Language()
    SoraSompengScript = Script()
    SouthAfrica = Country()
    SouthGeorgiaAndTheSouthSandwichIslands = Country()
    SouthKorea = Country()
    SouthNdebele = Language()
    SouthSudan = Country()
    SouthernSami = Language()
    SouthernSotho = Language()
    Spain = Country()
    Spanish = Language()
    SriLanka = Country()
    StandardMoroccanTamazight = Language()
    StandardQuotation = QuotationStyle()
    Sudan = Country()
    Sundanese = Language()
    SundaneseScript = Script()
    Suriname = Country()
    SvalbardAndJanMayenIslands = Country()
    Swahili = Language()
    Swati = Language()
    Swaziland = Country()
    Sweden = Country()
    Swedish = Language()
    SwissGerman = Language()
    Switzerland = Country()
    Sylheti = Language()
    SylotiNagriScript = Script()
    Syria = Country()
    Syriac = Language()
    SyriacScript = Script()
    SyrianArabRepublic = Country()
    Tachelhit = Language()
    Tagalog = Language()
    TagalogScript = Script()
    Tagbanwa = Language()
    TagbanwaScript = Script()
    Tahitian = Language()
    TaiDam = Language()
    TaiLeScript = Script()
    TaiNua = Language()
    TaiVietScript = Script()
    Taita = Language()
    Taiwan = Country()
    Tajik = Language()
    Tajikistan = Country()
    TakriScript = Script()
    Tamil = Language()
    TamilScript = Script()
    Tangut = Language()
    TangutScript = Script()
    Tanzania = Country()
    Taroko = Language()
    Tasawaq = Language()
    Tatar = Language()
    TedimChin = Language()
    Telugu = Language()
    TeluguScript = Script()
    Teso = Language()
    ThaanaScript = Script()
    Thai = Language()
    ThaiScript = Script()
    Thailand = Country()
    Tibetan = Language()
    TibetanScript = Script()
    TifinaghScript = Script()
    Tigre = Language()
    Tigrinya = Language()
    TirhutaScript = Script()
    Togo = Country()
    TokPisin = Language()
    Tokelau = Country()
    TokelauCountry = Country()
    TokelauLanguage = Language()
    Tonga = Country()
    Tongan = Language()
    TraditionalChineseScript = Script()
    TraditionalHanScript = Script()
    TrinidadAndTobago = Country()
    TristanDaCunha = Country()
    Tsonga = Language()
    Tswana = Language()
    Tunisia = Country()
    Turkey = Country()
    Turkish = Language()
    Turkmen = Language()
    Turkmenistan = Country()
    TurksAndCaicosIslands = Country()
    Tuvalu = Country()
    TuvaluCountry = Country()
    TuvaluLanguage = Language()
    Twi = Language()
    Tyap = Language()
    Uganda = Country()
    Ugaritic = Language()
    UgariticScript = Script()
    Uighur = Language()
    Uigur = Language()
    Ukraine = Country()
    Ukrainian = Language()
    UncodedLanguages = Language()
    UnitedArabEmirates = Country()
    UnitedKingdom = Country()
    UnitedStates = Country()
    UnitedStatesMinorOutlyingIslands = Country()
    UnitedStatesVirginIslands = Country()
    UpperSorbian = Language()
    Urdu = Language()
    Uruguay = Country()
    Uzbek = Language()
    Uzbekistan = Country()
    Vai = Language()
    VaiScript = Script()
    Vanuatu = Country()
    VarangKshitiScript = Script()
    VaticanCityState = Country()
    Venda = Language()
    Venezuela = Country()
    Vietnam = Country()
    Vietnamese = Language()
    Volapuk = Language()
    Vunjo = Language()
    Walamo = Language()
    WallisAndFutunaIslands = Country()
    Walloon = Language()
    Walser = Language()
    Warlpiri = Language()
    Welsh = Language()
    WesternFrisian = Language()
    WesternSahara = Country()
    Wolof = Language()
    Xhosa = Language()
    Yangben = Language()
    Yemen = Country()
    YiScript = Script()
    Yiddish = Language()
    Yoruba = Language()
    Zambia = Country()
    Zarma = Language()
    Zhuang = Language()
    Zimbabwe = Country()
    Zulu = Language()
    __class__ = QLocale
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QLocaleLanguage, country: QLocale.Country=QLocale.AnyCountry):
        'QLocale()\nQLocale(str)\nQLocale(QLocale.Language, country: QLocale.Country = QLocale.AnyCountry)\nQLocale(QLocale)\nQLocale(QLocale.Language, QLocale.Script, QLocale.Country)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def amText(cls, self):
        'amText(self) -> str'
        return ''
    
    @classmethod
    def bcp47Name(cls, self):
        'bcp47Name(self) -> str'
        return ''
    
    @classmethod
    def c(cls):
        'c() -> QLocale'
        pass
    
    @classmethod
    def country(cls, self):
        'country(self) -> QLocale.Country'
        pass
    
    @classmethod
    def countryToString(cls, QLocaleCountry):
        'countryToString(QLocale.Country) -> str'
        return ''
    
    @classmethod
    def createSeparatedList(cls, self, Iterablestr=None):
        'createSeparatedList(self, Iterable[str]) -> str'
        return ''
    
    @classmethod
    def currencySymbol(cls, self, format: QLocale.CurrencySymbolFormat=QLocale.CurrencySymbol):
        'currencySymbol(self, format: QLocale.CurrencySymbolFormat = QLocale.CurrencySymbol) -> str'
        return ''
    
    @classmethod
    def dateFormat(cls, self, format: QLocale.FormatType=QLocale.LongFormat):
        'dateFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def dateTimeFormat(cls, self, format: QLocale.FormatType=QLocale.LongFormat):
        'dateTimeFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def dayName(cls, self, int, format: QLocale.FormatType=QLocale.LongFormat):
        'dayName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def decimalPoint(cls, self):
        'decimalPoint(self) -> str'
        return ''
    
    @classmethod
    def exponential(cls, self):
        'exponential(self) -> str'
        return ''
    
    @classmethod
    def firstDayOfWeek(cls, self):
        'firstDayOfWeek(self) -> Qt.DayOfWeek'
        pass
    
    @classmethod
    def groupSeparator(cls, self):
        'groupSeparator(self) -> str'
        return ''
    
    @classmethod
    def language(cls, self):
        'language(self) -> QLocale.Language'
        pass
    
    @classmethod
    def languageToString(cls, QLocaleLanguage):
        'languageToString(QLocale.Language) -> str'
        return ''
    
    @classmethod
    def matchingLocales(cls, QLocaleLanguage, QLocaleScript, QLocaleCountry):
        'matchingLocales(QLocale.Language, QLocale.Script, QLocale.Country) -> object'
        pass
    
    @classmethod
    def measurementSystem(cls, self):
        'measurementSystem(self) -> QLocale.MeasurementSystem'
        pass
    
    @classmethod
    def monthName(cls, self, int, format: QLocale.FormatType=QLocale.LongFormat):
        'monthName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def nativeCountryName(cls, self):
        'nativeCountryName(self) -> str'
        return ''
    
    @classmethod
    def nativeLanguageName(cls, self):
        'nativeLanguageName(self) -> str'
        return ''
    
    @classmethod
    def negativeSign(cls, self):
        'negativeSign(self) -> str'
        return ''
    
    @classmethod
    def numberOptions(cls, self):
        'numberOptions(self) -> QLocale.NumberOptions'
        pass
    
    @classmethod
    def percent(cls, self):
        'percent(self) -> str'
        return ''
    
    @classmethod
    def pmText(cls, self):
        'pmText(self) -> str'
        return ''
    
    @classmethod
    def positiveSign(cls, self):
        'positiveSign(self) -> str'
        return ''
    
    @classmethod
    def quoteString(cls, self, str, style: QLocale.QuotationStyle=QLocale.StandardQuotation):
        'quoteString(self, str, style: QLocale.QuotationStyle = QLocale.StandardQuotation) -> str'
        return ''
    
    @classmethod
    def script(cls, self):
        'script(self) -> QLocale.Script'
        pass
    
    @classmethod
    def scriptToString(cls, QLocaleScript):
        'scriptToString(QLocale.Script) -> str'
        return ''
    
    @classmethod
    def setDefault(cls, QLocale):
        'setDefault(QLocale)'
        pass
    
    @classmethod
    def setNumberOptions(cls, self, UnionQLocaleNumberOptions=None, QLocaleNumberOption=None):
        'setNumberOptions(self, Union[QLocale.NumberOptions, QLocale.NumberOption])'
        pass
    
    @classmethod
    def standaloneDayName(cls, self, int, format: QLocale.FormatType=QLocale.LongFormat):
        'standaloneDayName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def standaloneMonthName(cls, self, int, format: QLocale.FormatType=QLocale.LongFormat):
        'standaloneMonthName(self, int, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def swap(cls, self, QLocale):
        'swap(self, QLocale)'
        pass
    
    @classmethod
    def system(cls):
        'system() -> QLocale'
        pass
    
    @classmethod
    def textDirection(cls, self):
        'textDirection(self) -> Qt.LayoutDirection'
        pass
    
    @classmethod
    def timeFormat(cls, self, format: QLocale.FormatType=QLocale.LongFormat):
        'timeFormat(self, format: QLocale.FormatType = QLocale.LongFormat) -> str'
        return ''
    
    @classmethod
    def toCurrencyString(cls, self, float, symbol: str=''):
        "toCurrencyString(self, float, symbol: str = '') -> str\ntoCurrencyString(self, float, str, int) -> str\ntoCurrencyString(self, int, symbol: str = '') -> str"
        return ''
    
    @classmethod
    def toDate(cls, self, str, format: QLocale.FormatType=QLocale.LongFormat):
        'toDate(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QDate\ntoDate(self, str, str) -> QDate'
        pass
    
    @classmethod
    def toDateTime(cls, self, str, format: QLocale.FormatType=QLocale.LongFormat):
        'toDateTime(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QDateTime\ntoDateTime(self, str, str) -> QDateTime'
        pass
    
    @classmethod
    def toDouble(cls, self, str):
        'toDouble(self, str) -> Tuple[float, bool]'
        pass
    
    @classmethod
    def toFloat(cls, self, str):
        'toFloat(self, str) -> Tuple[float, bool]'
        pass
    
    @classmethod
    def toInt(cls, self, str):
        'toInt(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toLongLong(cls, self, str):
        'toLongLong(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toLower(cls, self, str):
        'toLower(self, str) -> str'
        return ''
    
    @classmethod
    def toShort(cls, self, str):
        'toShort(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toString(cls, self, UnionQDateTime=None, datetimedatetime=None, format: QLocale.FormatType=QLocale.LongFormat):
        "toString(self, float, format: str = 'g', precision: int = 6) -> str\ntoString(self, Union[QDateTime, datetime.datetime], str) -> str\ntoString(self, Union[QDateTime, datetime.datetime], format: QLocale.FormatType = QLocale.LongFormat) -> str\ntoString(self, Union[QDate, datetime.date], str) -> str\ntoString(self, Union[QDate, datetime.date], format: QLocale.FormatType = QLocale.LongFormat) -> str\ntoString(self, Union[QTime, datetime.time], str) -> str\ntoString(self, Union[QTime, datetime.time], format: QLocale.FormatType = QLocale.LongFormat) -> str\ntoString(self, int) -> str"
        return ''
    
    @classmethod
    def toTime(cls, self, str, format: QLocale.FormatType=QLocale.LongFormat):
        'toTime(self, str, format: QLocale.FormatType = QLocale.LongFormat) -> QTime\ntoTime(self, str, str) -> QTime'
        pass
    
    @classmethod
    def toUInt(cls, self, str):
        'toUInt(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toULongLong(cls, self, str):
        'toULongLong(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toUShort(cls, self, str):
        'toUShort(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def toUpper(cls, self, str):
        'toUpper(self, str) -> str'
        return ''
    
    @classmethod
    def uiLanguages(cls, self):
        'uiLanguages(self) -> List[str]'
        pass
    
    @classmethod
    def weekdays(cls, self):
        'weekdays(self) -> List[Qt.DayOfWeek]'
        pass
    
    @classmethod
    def zeroDigit(cls, self):
        'zeroDigit(self) -> str'
        return ''
    

class QLockFile(_mod_sip.simplewrapper):
    'QLockFile(str)'
    LockError = LockError
    LockFailedError = LockError()
    NoError = LockError()
    PermissionError = LockError()
    UnknownError = LockError()
    __class__ = QLockFile
    __dict__ = {}
    def __init__(self, str):
        'QLockFile(str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QLockFile.LockError'
        pass
    
    @classmethod
    def getLockInfo(cls, self):
        'getLockInfo(self) -> Tuple[bool, int, str, str]'
        pass
    
    @classmethod
    def isLocked(cls, self):
        'isLocked(self) -> bool'
        return True
    
    @classmethod
    def lock(cls, self):
        'lock(self) -> bool'
        return True
    
    @classmethod
    def removeStaleLockFile(cls, self):
        'removeStaleLockFile(self) -> bool'
        return True
    
    @classmethod
    def setStaleLockTime(cls, self, int):
        'setStaleLockTime(self, int)'
        pass
    
    @classmethod
    def staleLockTime(cls, self):
        'staleLockTime(self) -> int'
        return 1
    
    @classmethod
    def tryLock(cls, self, timeout: int=0):
        'tryLock(self, timeout: int = 0) -> bool'
        return True
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QMargins(_mod_sip.simplewrapper):
    'QMargins()\nQMargins(int, int, int, int)\nQMargins(QMargins)'
    def __add__(self, value):
        'Return self+value.'
        return QMargins()
    
    __class__ = QMargins
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, int, int_, int_1, int_2):
        'QMargins()\nQMargins(int, int, int, int)\nQMargins(QMargins)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QMargins()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return QMargins()
    
    def __pos__(self):
        '+self'
        return QMargins()
    
    def __radd__(self, value):
        'Return value+self.'
        return QMargins()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QMargins()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QMargins()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QMargins()
    
    def __sub__(self, value):
        'Return self-value.'
        return QMargins()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def bottom(cls, self):
        'bottom(self) -> int'
        return 1
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def left(cls, self):
        'left(self) -> int'
        return 1
    
    @classmethod
    def right(cls, self):
        'right(self) -> int'
        return 1
    
    @classmethod
    def setBottom(cls, self, int):
        'setBottom(self, int)'
        pass
    
    @classmethod
    def setLeft(cls, self, int):
        'setLeft(self, int)'
        pass
    
    @classmethod
    def setRight(cls, self, int):
        'setRight(self, int)'
        pass
    
    @classmethod
    def setTop(cls, self, int):
        'setTop(self, int)'
        pass
    
    @classmethod
    def top(cls, self):
        'top(self) -> int'
        return 1
    

class QMarginsF(_mod_sip.simplewrapper):
    'QMarginsF()\nQMarginsF(float, float, float, float)\nQMarginsF(QMargins)\nQMarginsF(QMarginsF)'
    def __add__(self, value):
        'Return self+value.'
        return QMarginsF()
    
    __class__ = QMarginsF
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, float, float_, float_1, float_2):
        'QMarginsF()\nQMarginsF(float, float, float, float)\nQMarginsF(QMargins)\nQMarginsF(QMarginsF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QMarginsF()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return QMarginsF()
    
    def __pos__(self):
        '+self'
        return QMarginsF()
    
    def __radd__(self, value):
        'Return value+self.'
        return QMarginsF()
    
    def __rmul__(self, value):
        'Return value*self.'
        return QMarginsF()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QMarginsF()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QMarginsF()
    
    def __sub__(self, value):
        'Return self-value.'
        return QMarginsF()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def bottom(cls, self):
        'bottom(self) -> float'
        return 1.0
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def left(cls, self):
        'left(self) -> float'
        return 1.0
    
    @classmethod
    def right(cls, self):
        'right(self) -> float'
        return 1.0
    
    @classmethod
    def setBottom(cls, self, float):
        'setBottom(self, float)'
        pass
    
    @classmethod
    def setLeft(cls, self, float):
        'setLeft(self, float)'
        pass
    
    @classmethod
    def setRight(cls, self, float):
        'setRight(self, float)'
        pass
    
    @classmethod
    def setTop(cls, self, float):
        'setTop(self, float)'
        pass
    
    @classmethod
    def toMargins(cls, self):
        'toMargins(self) -> QMargins'
        pass
    
    @classmethod
    def top(cls, self):
        'top(self) -> float'
        return 1.0
    

class QMessageAuthenticationCode(_mod_sip.simplewrapper):
    'QMessageAuthenticationCode(QCryptographicHash.Algorithm, key: Union[QByteArray, bytes, bytearray] = QByteArray())'
    __class__ = QMessageAuthenticationCode
    __dict__ = {}
    def __init__(self, QCryptographicHashAlgorithm, key: Union[QByteArray,bytes,bytearray]=QByteArray()):
        'QMessageAuthenticationCode(QCryptographicHash.Algorithm, key: Union[QByteArray, bytes, bytearray] = QByteArray())'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addData(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'addData(self, str, int)\naddData(self, Union[QByteArray, bytes, bytearray])\naddData(self, QIODevice) -> bool'
        pass
    
    @classmethod
    def hash(cls, UnionQByteArray=None, bytes=None, bytearray=None, UnionQByteArray_=None, bytes_=None, bytearray_=None, QCryptographicHashAlgorithm=None):
        'hash(Union[QByteArray, bytes, bytearray], Union[QByteArray, bytes, bytearray], QCryptographicHash.Algorithm) -> QByteArray'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self)'
        pass
    
    @classmethod
    def result(cls, self):
        'result(self) -> QByteArray'
        pass
    
    @classmethod
    def setKey(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'setKey(self, Union[QByteArray, bytes, bytearray])'
        pass
    

class QMessageLogContext(_mod_sip.simplewrapper):
    __class__ = QMessageLogContext
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class QMessageLogger(_mod_sip.simplewrapper):
    'QMessageLogger()\nQMessageLogger(str, int, str)\nQMessageLogger(str, int, str, str)'
    __class__ = QMessageLogger
    __dict__ = {}
    def __init__(self, str, int, str_, str_1):
        'QMessageLogger()\nQMessageLogger(str, int, str)\nQMessageLogger(str, int, str, str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def critical(cls, self, str):
        'critical(self, str)'
        pass
    
    @classmethod
    def debug(cls, self, str):
        'debug(self, str)'
        pass
    
    @classmethod
    def fatal(cls, self, str):
        'fatal(self, str)'
        pass
    
    @classmethod
    def info(cls, self, str):
        'info(self, str)'
        pass
    
    @classmethod
    def warning(cls, self, str):
        'warning(self, str)'
        pass
    

class QMetaClassInfo(_mod_sip.simplewrapper):
    'QMetaClassInfo()\nQMetaClassInfo(QMetaClassInfo)'
    __class__ = QMetaClassInfo
    __dict__ = {}
    def __init__(self, QMetaClassInfo):
        'QMetaClassInfo()\nQMetaClassInfo(QMetaClassInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def value(cls, self):
        'value(self) -> str'
        return ''
    

class QMetaEnum(_mod_sip.simplewrapper):
    'QMetaEnum()\nQMetaEnum(QMetaEnum)'
    __class__ = QMetaEnum
    __dict__ = {}
    def __init__(self, QMetaEnum):
        'QMetaEnum()\nQMetaEnum(QMetaEnum)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def isFlag(cls, self):
        'isFlag(self) -> bool'
        return True
    
    @classmethod
    def isScoped(cls, self):
        'isScoped(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def key(cls, self, int):
        'key(self, int) -> str'
        return ''
    
    @classmethod
    def keyCount(cls, self):
        'keyCount(self) -> int'
        return 1
    
    @classmethod
    def keyToValue(cls, self, str):
        'keyToValue(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def keysToValue(cls, self, str):
        'keysToValue(self, str) -> Tuple[int, bool]'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def scope(cls, self):
        'scope(self) -> str'
        return ''
    
    @classmethod
    def value(cls, self, int):
        'value(self, int) -> int'
        return 1
    
    @classmethod
    def valueToKey(cls, self, int):
        'valueToKey(self, int) -> str'
        return ''
    
    @classmethod
    def valueToKeys(cls, self, int):
        'valueToKeys(self, int) -> QByteArray'
        pass
    

class QMetaMethod(_mod_sip.simplewrapper):
    'QMetaMethod()\nQMetaMethod(QMetaMethod)'
    Access = Access
    Constructor = MethodType()
    Method = MethodType()
    MethodType = MethodType
    Private = Access()
    Protected = Access()
    Public = Access()
    Signal = MethodType()
    Slot = MethodType()
    __class__ = QMetaMethod
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QMetaMethod):
        'QMetaMethod()\nQMetaMethod(QMetaMethod)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def access(cls, self):
        'access(self) -> QMetaMethod.Access'
        pass
    
    @classmethod
    def invoke(cls, self, QObject, QtConnectionType, QGenericReturnArgument, value0: QGenericArgument=QGenericArgument(0,0), value1: QGenericArgument=QGenericArgument(0,0), value2: QGenericArgument=QGenericArgument(0,0), value3: QGenericArgument=QGenericArgument(0,0), value4: QGenericArgument=QGenericArgument(0,0), value5: QGenericArgument=QGenericArgument(0,0), value6: QGenericArgument=QGenericArgument(0,0), value7: QGenericArgument=QGenericArgument(0,0), value8: QGenericArgument=QGenericArgument(0,0), value9: QGenericArgument=QGenericArgument(0,0)):
        'invoke(self, QObject, Qt.ConnectionType, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvoke(self, QObject, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvoke(self, QObject, Qt.ConnectionType, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvoke(self, QObject, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object'
        pass
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def methodIndex(cls, self):
        'methodIndex(self) -> int'
        return 1
    
    @classmethod
    def methodSignature(cls, self):
        'methodSignature(self) -> QByteArray'
        pass
    
    @classmethod
    def methodType(cls, self):
        'methodType(self) -> QMetaMethod.MethodType'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> QByteArray'
        pass
    
    @classmethod
    def parameterCount(cls, self):
        'parameterCount(self) -> int'
        return 1
    
    @classmethod
    def parameterNames(cls, self):
        'parameterNames(self) -> List[QByteArray]'
        pass
    
    @classmethod
    def parameterType(cls, self, int):
        'parameterType(self, int) -> int'
        return 1
    
    @classmethod
    def parameterTypes(cls, self):
        'parameterTypes(self) -> List[QByteArray]'
        pass
    
    @classmethod
    def returnType(cls, self):
        'returnType(self) -> int'
        return 1
    
    @classmethod
    def tag(cls, self):
        'tag(self) -> str'
        return ''
    
    @classmethod
    def typeName(cls, self):
        'typeName(self) -> str'
        return ''
    

class QMetaObject(_mod_sip.simplewrapper):
    'QMetaObject()\nQMetaObject(QMetaObject)'
    __class__ = QMetaObject
    __dict__ = {}
    def __init__(self, QMetaObject):
        'QMetaObject()\nQMetaObject(QMetaObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def checkConnectArgs(cls, QMetaMethod, QMetaMethod_):
        'checkConnectArgs(str, str) -> bool\ncheckConnectArgs(QMetaMethod, QMetaMethod) -> bool'
        return True
    
    @classmethod
    def classInfo(cls, self, int):
        'classInfo(self, int) -> QMetaClassInfo'
        pass
    
    @classmethod
    def classInfoCount(cls, self):
        'classInfoCount(self) -> int'
        return 1
    
    @classmethod
    def classInfoOffset(cls, self):
        'classInfoOffset(self) -> int'
        return 1
    
    @classmethod
    def className(cls, self):
        'className(self) -> str'
        return ''
    
    @classmethod
    def connectSlotsByName(cls, QObject):
        'connectSlotsByName(QObject)'
        pass
    
    @classmethod
    def constructor(cls, self, int):
        'constructor(self, int) -> QMetaMethod'
        pass
    
    @classmethod
    def constructorCount(cls, self):
        'constructorCount(self) -> int'
        return 1
    
    @classmethod
    def enumerator(cls, self, int):
        'enumerator(self, int) -> QMetaEnum'
        pass
    
    @classmethod
    def enumeratorCount(cls, self):
        'enumeratorCount(self) -> int'
        return 1
    
    @classmethod
    def enumeratorOffset(cls, self):
        'enumeratorOffset(self) -> int'
        return 1
    
    @classmethod
    def indexOfClassInfo(cls, self, str):
        'indexOfClassInfo(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfConstructor(cls, self, str):
        'indexOfConstructor(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfEnumerator(cls, self, str):
        'indexOfEnumerator(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfMethod(cls, self, str):
        'indexOfMethod(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfProperty(cls, self, str):
        'indexOfProperty(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfSignal(cls, self, str):
        'indexOfSignal(self, str) -> int'
        return 1
    
    @classmethod
    def indexOfSlot(cls, self, str):
        'indexOfSlot(self, str) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, QMetaObject):
        'inherits(self, QMetaObject) -> bool'
        return True
    
    @classmethod
    def invokeMethod(cls, QObject, str, QtConnectionType, QGenericReturnArgument, value0: QGenericArgument=QGenericArgument(0,0), value1: QGenericArgument=QGenericArgument(0,0), value2: QGenericArgument=QGenericArgument(0,0), value3: QGenericArgument=QGenericArgument(0,0), value4: QGenericArgument=QGenericArgument(0,0), value5: QGenericArgument=QGenericArgument(0,0), value6: QGenericArgument=QGenericArgument(0,0), value7: QGenericArgument=QGenericArgument(0,0), value8: QGenericArgument=QGenericArgument(0,0), value9: QGenericArgument=QGenericArgument(0,0)):
        'invokeMethod(QObject, str, Qt.ConnectionType, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvokeMethod(QObject, str, QGenericReturnArgument, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvokeMethod(QObject, str, Qt.ConnectionType, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object\ninvokeMethod(QObject, str, value0: QGenericArgument = QGenericArgument(0,0), value1: QGenericArgument = QGenericArgument(0,0), value2: QGenericArgument = QGenericArgument(0,0), value3: QGenericArgument = QGenericArgument(0,0), value4: QGenericArgument = QGenericArgument(0,0), value5: QGenericArgument = QGenericArgument(0,0), value6: QGenericArgument = QGenericArgument(0,0), value7: QGenericArgument = QGenericArgument(0,0), value8: QGenericArgument = QGenericArgument(0,0), value9: QGenericArgument = QGenericArgument(0,0)) -> object'
        pass
    
    @classmethod
    def method(cls, self, int):
        'method(self, int) -> QMetaMethod'
        pass
    
    @classmethod
    def methodCount(cls, self):
        'methodCount(self) -> int'
        return 1
    
    @classmethod
    def methodOffset(cls, self):
        'methodOffset(self) -> int'
        return 1
    
    @classmethod
    def normalizedSignature(cls, str):
        'normalizedSignature(str) -> QByteArray'
        pass
    
    @classmethod
    def normalizedType(cls, str):
        'normalizedType(str) -> QByteArray'
        pass
    
    @classmethod
    def property(cls, self, int):
        'property(self, int) -> QMetaProperty'
        pass
    
    @classmethod
    def propertyCount(cls, self):
        'propertyCount(self) -> int'
        return 1
    
    @classmethod
    def propertyOffset(cls, self):
        'propertyOffset(self) -> int'
        return 1
    
    @classmethod
    def superClass(cls, self):
        'superClass(self) -> QMetaObject'
        pass
    
    @classmethod
    def userProperty(cls, self):
        'userProperty(self) -> QMetaProperty'
        pass
    

class QMetaProperty(_mod_sip.simplewrapper):
    'QMetaProperty()\nQMetaProperty(QMetaProperty)'
    __class__ = QMetaProperty
    __dict__ = {}
    def __init__(self, QMetaProperty):
        'QMetaProperty()\nQMetaProperty(QMetaProperty)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def enumerator(cls, self):
        'enumerator(self) -> QMetaEnum'
        pass
    
    @classmethod
    def hasNotifySignal(cls, self):
        'hasNotifySignal(self) -> bool'
        return True
    
    @classmethod
    def hasStdCppSet(cls, self):
        'hasStdCppSet(self) -> bool'
        return True
    
    @classmethod
    def isConstant(cls, self):
        'isConstant(self) -> bool'
        return True
    
    @classmethod
    def isDesignable(cls, self, object: QObject=None):
        'isDesignable(self, object: QObject = None) -> bool'
        return True
    
    @classmethod
    def isEnumType(cls, self):
        'isEnumType(self) -> bool'
        return True
    
    @classmethod
    def isFinal(cls, self):
        'isFinal(self) -> bool'
        return True
    
    @classmethod
    def isFlagType(cls, self):
        'isFlagType(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isResettable(cls, self):
        'isResettable(self) -> bool'
        return True
    
    @classmethod
    def isScriptable(cls, self, object: QObject=None):
        'isScriptable(self, object: QObject = None) -> bool'
        return True
    
    @classmethod
    def isStored(cls, self, object: QObject=None):
        'isStored(self, object: QObject = None) -> bool'
        return True
    
    @classmethod
    def isUser(cls, self, object: QObject=None):
        'isUser(self, object: QObject = None) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def notifySignal(cls, self):
        'notifySignal(self) -> QMetaMethod'
        pass
    
    @classmethod
    def notifySignalIndex(cls, self):
        'notifySignalIndex(self) -> int'
        return 1
    
    @classmethod
    def propertyIndex(cls, self):
        'propertyIndex(self) -> int'
        return 1
    
    @classmethod
    def read(cls, self, QObject):
        'read(self, QObject) -> Any'
        pass
    
    @classmethod
    def reset(cls, self, QObject):
        'reset(self, QObject) -> bool'
        return True
    
    @classmethod
    def type(cls, self):
        'type(self) -> QVariant.Type'
        pass
    
    @classmethod
    def typeName(cls, self):
        'typeName(self) -> str'
        return ''
    
    @classmethod
    def userType(cls, self):
        'userType(self) -> int'
        return 1
    
    @classmethod
    def write(cls, self, QObject, Any):
        'write(self, QObject, Any) -> bool'
        return True
    

class QMetaType(_mod_sip.simplewrapper):
    'QMetaType(int)'
    Bool = Type()
    Char = Type()
    Double = Type()
    FirstGuiType = Type()
    Float = Type()
    Int = Type()
    IsGadget = TypeFlag()
    LastCoreType = Type()
    Long = Type()
    LongLong = Type()
    MovableType = TypeFlag()
    NeedsConstruction = TypeFlag()
    NeedsDestruction = TypeFlag()
    QBitArray = Type()
    QBitmap = Type()
    QBrush = Type()
    QByteArray = Type()
    QByteArrayList = Type()
    QChar = Type()
    QColor = Type()
    QCursor = Type()
    QDate = Type()
    QDateTime = Type()
    QEasingCurve = Type()
    QFont = Type()
    QIcon = Type()
    QImage = Type()
    QJsonArray = Type()
    QJsonDocument = Type()
    QJsonObject = Type()
    QJsonValue = Type()
    QKeySequence = Type()
    QLine = Type()
    QLineF = Type()
    QLocale = Type()
    QMatrix = Type()
    QMatrix4x4 = Type()
    QModelIndex = Type()
    QObjectStar = Type()
    QPalette = Type()
    QPen = Type()
    QPersistentModelIndex = Type()
    QPixmap = Type()
    QPoint = Type()
    QPointF = Type()
    QPolygon = Type()
    QPolygonF = Type()
    QQuaternion = Type()
    QRect = Type()
    QRectF = Type()
    QRegExp = Type()
    QRegion = Type()
    QRegularExpression = Type()
    QSize = Type()
    QSizeF = Type()
    QSizePolicy = Type()
    QString = Type()
    QStringList = Type()
    QTextFormat = Type()
    QTextLength = Type()
    QTime = Type()
    QTransform = Type()
    QUrl = Type()
    QUuid = Type()
    QVariant = Type()
    QVariantHash = Type()
    QVariantList = Type()
    QVariantMap = Type()
    QVector2D = Type()
    QVector3D = Type()
    QVector4D = Type()
    SChar = Type()
    Short = Type()
    Type = Type
    TypeFlag = TypeFlag
    TypeFlags = TypeFlags
    UChar = Type()
    UInt = Type()
    ULong = Type()
    ULongLong = Type()
    UShort = Type()
    UnknownType = Type()
    User = Type()
    Void = Type()
    VoidStar = Type()
    __class__ = QMetaType
    __dict__ = {}
    def __init__(self, int):
        'QMetaType(int)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def flags(cls, self):
        'flags(self) -> QMetaType.TypeFlags'
        pass
    
    @classmethod
    def isRegistered(cls, self):
        'isRegistered(int) -> bool\nisRegistered(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def metaObjectForType(cls, int):
        'metaObjectForType(int) -> QMetaObject'
        pass
    
    @classmethod
    def type(cls, str):
        'type(str) -> int'
        return 1
    
    @classmethod
    def typeFlags(cls, int):
        'typeFlags(int) -> QMetaType.TypeFlags'
        pass
    
    @classmethod
    def typeName(cls, int):
        'typeName(int) -> str'
        return ''
    

class QMimeData(QObject):
    'QMimeData()'
    __class__ = QMimeData
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self):
        'QMimeData()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def colorData(cls, self):
        'colorData(self) -> Any'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, str):
        'data(self, str) -> QByteArray'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def formats(cls, self):
        'formats(self) -> List[str]'
        pass
    
    @classmethod
    def hasColor(cls, self):
        'hasColor(self) -> bool'
        return True
    
    @classmethod
    def hasFormat(cls, self, str):
        'hasFormat(self, str) -> bool'
        return True
    
    @classmethod
    def hasHtml(cls, self):
        'hasHtml(self) -> bool'
        return True
    
    @classmethod
    def hasImage(cls, self):
        'hasImage(self) -> bool'
        return True
    
    @classmethod
    def hasText(cls, self):
        'hasText(self) -> bool'
        return True
    
    @classmethod
    def hasUrls(cls, self):
        'hasUrls(self) -> bool'
        return True
    
    @classmethod
    def html(cls, self):
        'html(self) -> str'
        return ''
    
    @classmethod
    def imageData(cls, self):
        'imageData(self) -> Any'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeFormat(cls, self, str):
        'removeFormat(self, str)'
        pass
    
    @classmethod
    def retrieveData(cls, self, str, QVariantType):
        'retrieveData(self, str, QVariant.Type) -> Any'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setColorData(cls, self, Any):
        'setColorData(self, Any)'
        pass
    
    @classmethod
    def setData(cls, self, str, UnionQByteArray=None, bytes=None, bytearray=None):
        'setData(self, str, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def setHtml(cls, self, str):
        'setHtml(self, str)'
        pass
    
    @classmethod
    def setImageData(cls, self, Any):
        'setImageData(self, Any)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setText(cls, self, str):
        'setText(self, str)'
        pass
    
    @classmethod
    def setUrls(cls, self, IterableQUrl=None):
        'setUrls(self, Iterable[QUrl])'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def text(cls, self):
        'text(self) -> str'
        return ''
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def urls(cls, self):
        'urls(self) -> object'
        pass
    

class QMimeDatabase(_mod_sip.simplewrapper):
    'QMimeDatabase()'
    MatchContent = MatchMode()
    MatchDefault = MatchMode()
    MatchExtension = MatchMode()
    MatchMode = MatchMode
    __class__ = QMimeDatabase
    __dict__ = {}
    def __init__(self):
        'QMimeDatabase()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def allMimeTypes(cls, self):
        'allMimeTypes(self) -> List[QMimeType]'
        pass
    
    @classmethod
    def mimeTypeForData(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'mimeTypeForData(self, Union[QByteArray, bytes, bytearray]) -> QMimeType\nmimeTypeForData(self, QIODevice) -> QMimeType'
        pass
    
    @classmethod
    def mimeTypeForFile(cls, self, QFileInfo, mode: QMimeDatabase.MatchMode=QMimeDatabase.MatchDefault):
        'mimeTypeForFile(self, str, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType\nmimeTypeForFile(self, QFileInfo, mode: QMimeDatabase.MatchMode = QMimeDatabase.MatchDefault) -> QMimeType'
        pass
    
    @classmethod
    def mimeTypeForFileNameAndData(cls, self, str, UnionQByteArray=None, bytes=None, bytearray=None):
        'mimeTypeForFileNameAndData(self, str, QIODevice) -> QMimeType\nmimeTypeForFileNameAndData(self, str, Union[QByteArray, bytes, bytearray]) -> QMimeType'
        pass
    
    @classmethod
    def mimeTypeForName(cls, self, str):
        'mimeTypeForName(self, str) -> QMimeType'
        pass
    
    @classmethod
    def mimeTypeForUrl(cls, self, QUrl):
        'mimeTypeForUrl(self, QUrl) -> QMimeType'
        pass
    
    @classmethod
    def mimeTypesForFileName(cls, self, str):
        'mimeTypesForFileName(self, str) -> object'
        pass
    
    @classmethod
    def suffixForFileName(cls, self, str):
        'suffixForFileName(self, str) -> str'
        return ''
    

class QMimeType(_mod_sip.simplewrapper):
    'QMimeType()\nQMimeType(QMimeType)'
    __class__ = QMimeType
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QMimeType):
        'QMimeType()\nQMimeType(QMimeType)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def aliases(cls, self):
        'aliases(self) -> List[str]'
        pass
    
    @classmethod
    def allAncestors(cls, self):
        'allAncestors(self) -> List[str]'
        pass
    
    @classmethod
    def comment(cls, self):
        'comment(self) -> str'
        return ''
    
    @classmethod
    def filterString(cls, self):
        'filterString(self) -> str'
        return ''
    
    @classmethod
    def genericIconName(cls, self):
        'genericIconName(self) -> str'
        return ''
    
    @classmethod
    def globPatterns(cls, self):
        'globPatterns(self) -> List[str]'
        pass
    
    @classmethod
    def iconName(cls, self):
        'iconName(self) -> str'
        return ''
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def isDefault(cls, self):
        'isDefault(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def parentMimeTypes(cls, self):
        'parentMimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def preferredSuffix(cls, self):
        'preferredSuffix(self) -> str'
        return ''
    
    @classmethod
    def suffixes(cls, self):
        'suffixes(self) -> List[str]'
        pass
    
    @classmethod
    def swap(cls, self, QMimeType):
        'swap(self, QMimeType)'
        pass
    

class QModelIndex(_mod_sip.simplewrapper):
    'QModelIndex()\nQModelIndex(QModelIndex)\nQModelIndex(QPersistentModelIndex)'
    __class__ = QModelIndex
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QPersistentModelIndex):
        'QModelIndex()\nQModelIndex(QModelIndex)\nQModelIndex(QPersistentModelIndex)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def child(cls, self, int, int_):
        'child(self, int, int) -> QModelIndex'
        pass
    
    @classmethod
    def column(cls, self):
        'column(self) -> int'
        return 1
    
    @classmethod
    def data(cls, self, role: int=Qt.DisplayRole):
        'data(self, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def flags(cls, self):
        'flags(self) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def internalId(cls, self):
        'internalId(self) -> int'
        return 1
    
    @classmethod
    def internalPointer(cls, self):
        'internalPointer(self) -> object'
        pass
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def model(cls, self):
        'model(self) -> QAbstractItemModel'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QModelIndex'
        pass
    
    @classmethod
    def row(cls, self):
        'row(self) -> int'
        return 1
    
    @classmethod
    def sibling(cls, self, int, int_):
        'sibling(self, int, int) -> QModelIndex'
        pass
    

class QMutex(_mod_sip.simplewrapper):
    'QMutex(mode: QMutex.RecursionMode = QMutex.NonRecursive)'
    NonRecursive = RecursionMode()
    RecursionMode = RecursionMode
    Recursive = RecursionMode()
    __class__ = QMutex
    __dict__ = {}
    def __init__(self, mode: QMutex.RecursionMode=QMutex.NonRecursive):
        'QMutex(mode: QMutex.RecursionMode = QMutex.NonRecursive)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def isRecursive(cls, self):
        'isRecursive(self) -> bool'
        return True
    
    @classmethod
    def lock(cls, self):
        'lock(self)'
        pass
    
    @classmethod
    def tryLock(cls, self, timeout: int=0):
        'tryLock(self, timeout: int = 0) -> bool'
        return True
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QMutexLocker(_mod_sip.simplewrapper):
    'QMutexLocker(QMutex)'
    __class__ = QMutexLocker
    __dict__ = {}
    @classmethod
    def __enter__(cls, self):
        '__enter__(self) -> object'
        return self
    
    @classmethod
    def __exit__(cls, self, object, object_, object_1):
        '__exit__(self, object, object, object)'
        pass
    
    def __init__(self, QMutex):
        'QMutexLocker(QMutex)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def mutex(cls, self):
        'mutex(self) -> QMutex'
        pass
    
    @classmethod
    def relock(cls, self):
        'relock(self)'
        pass
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QObject(_mod_sip.wrapper):
    'QObject(parent: QObject = None)'
    __class__ = QObject
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QObject(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls, self, QChildEvent):
        'childEvent(self, QChildEvent)'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls, self, QMetaMethod):
        'connectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def customEvent(cls, self, QEvent):
        'customEvent(self, QEvent)'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    def destroyed(self, QObject=None):
        'destroyed(self, QObject = None) [signal]'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls, self, QMetaMethod):
        'disconnectNotify(self, QMetaMethod)'
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls, self, QMetaMethod):
        'isSignalConnected(self, QMetaMethod) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    def objectNameChanged(self, str):
        'objectNameChanged(self, str) [signal]'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls, self, PYQT_SIGNAL):
        'receivers(self, PYQT_SIGNAL) -> int'
        return 1
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls, self):
        'sender(self) -> QObject'
        pass
    
    @classmethod
    def senderSignalIndex(cls, self):
        'senderSignalIndex(self) -> int'
        return 1
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QObjectCleanupHandler(QObject):
    'QObjectCleanupHandler()'
    __class__ = QObjectCleanupHandler
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self):
        'QObjectCleanupHandler()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def add(cls, self, QObject):
        'add(self, QObject) -> QObject'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def remove(cls, self, QObject):
        'remove(self, QObject)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QOperatingSystemVersion(_mod_sip.simplewrapper):
    'QOperatingSystemVersion(QOperatingSystemVersion.OSType, int, vminor: int = -1, vmicro: int = -1)\nQOperatingSystemVersion(QOperatingSystemVersion)'
    Android = OSType()
    AndroidJellyBean = QOperatingSystemVersion()
    AndroidJellyBean_MR1 = QOperatingSystemVersion()
    AndroidJellyBean_MR2 = QOperatingSystemVersion()
    AndroidKitKat = QOperatingSystemVersion()
    AndroidLollipop = QOperatingSystemVersion()
    AndroidLollipop_MR1 = QOperatingSystemVersion()
    AndroidMarshmallow = QOperatingSystemVersion()
    AndroidNougat = QOperatingSystemVersion()
    AndroidNougat_MR1 = QOperatingSystemVersion()
    AndroidOreo = QOperatingSystemVersion()
    IOS = OSType()
    MacOS = OSType()
    MacOSHighSierra = QOperatingSystemVersion()
    MacOSSierra = QOperatingSystemVersion()
    OSType = OSType
    OSXElCapitan = QOperatingSystemVersion()
    OSXMavericks = QOperatingSystemVersion()
    OSXYosemite = QOperatingSystemVersion()
    TvOS = OSType()
    Unknown = OSType()
    WatchOS = OSType()
    Windows = OSType()
    Windows10 = QOperatingSystemVersion()
    Windows7 = QOperatingSystemVersion()
    Windows8 = QOperatingSystemVersion()
    Windows8_1 = QOperatingSystemVersion()
    __class__ = QOperatingSystemVersion
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QOperatingSystemVersionOSType, int, vminor: int=-1, vmicro: int=-1):
        'QOperatingSystemVersion(QOperatingSystemVersion.OSType, int, vminor: int = -1, vmicro: int = -1)\nQOperatingSystemVersion(QOperatingSystemVersion)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def current(cls):
        'current() -> QOperatingSystemVersion'
        pass
    
    @classmethod
    def majorVersion(cls, self):
        'majorVersion(self) -> int'
        return 1
    
    @classmethod
    def microVersion(cls, self):
        'microVersion(self) -> int'
        return 1
    
    @classmethod
    def minorVersion(cls, self):
        'minorVersion(self) -> int'
        return 1
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def segmentCount(cls, self):
        'segmentCount(self) -> int'
        return 1
    
    @classmethod
    def type(cls, self):
        'type(self) -> QOperatingSystemVersion.OSType'
        pass
    

class QParallelAnimationGroup(QAnimationGroup):
    'QParallelAnimationGroup(parent: QObject = None)'
    __class__ = QParallelAnimationGroup
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QParallelAnimationGroup(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def animationAt(cls, self, int):
        'animationAt(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def animationCount(cls, self):
        'animationCount(self) -> int'
        return 1
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def indexOfAnimation(cls, self, QAbstractAnimation):
        'indexOfAnimation(self, QAbstractAnimation) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertAnimation(cls, self, int, QAbstractAnimation):
        'insertAnimation(self, int, QAbstractAnimation)'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def takeAnimation(cls, self, int):
        'takeAnimation(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls, self, int):
        'updateCurrentTime(self, int)'
        pass
    
    @classmethod
    def updateDirection(cls, self, QAbstractAnimationDirection):
        'updateDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def updateState(cls, self, QAbstractAnimationState, QAbstractAnimationState_):
        'updateState(self, QAbstractAnimation.State, QAbstractAnimation.State)'
        pass
    

class QPauseAnimation(QAbstractAnimation):
    'QPauseAnimation(parent: QObject = None)\nQPauseAnimation(int, parent: QObject = None)'
    __class__ = QPauseAnimation
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, int, parent: QObject=None):
        'QPauseAnimation(parent: QObject = None)\nQPauseAnimation(int, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setDuration(cls, self, int):
        'setDuration(self, int)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls, self, int):
        'updateCurrentTime(self, int)'
        pass
    
    @classmethod
    def updateDirection(cls):
        pass
    
    @classmethod
    def updateState(cls):
        pass
    

class QPersistentModelIndex(_mod_sip.simplewrapper):
    'QPersistentModelIndex()\nQPersistentModelIndex(QModelIndex)\nQPersistentModelIndex(QPersistentModelIndex)'
    __class__ = QPersistentModelIndex
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QPersistentModelIndex):
        'QPersistentModelIndex()\nQPersistentModelIndex(QModelIndex)\nQPersistentModelIndex(QPersistentModelIndex)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def child(cls, self, int, int_):
        'child(self, int, int) -> QModelIndex'
        pass
    
    @classmethod
    def column(cls, self):
        'column(self) -> int'
        return 1
    
    @classmethod
    def data(cls, self, role: int=Qt.DisplayRole):
        'data(self, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def flags(cls, self):
        'flags(self) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def model(cls, self):
        'model(self) -> QAbstractItemModel'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QModelIndex'
        pass
    
    @classmethod
    def row(cls, self):
        'row(self) -> int'
        return 1
    
    @classmethod
    def sibling(cls, self, int, int_):
        'sibling(self, int, int) -> QModelIndex'
        pass
    
    @classmethod
    def swap(cls, self, QPersistentModelIndex):
        'swap(self, QPersistentModelIndex)'
        pass
    

class QPluginLoader(QObject):
    'QPluginLoader(parent: QObject = None)\nQPluginLoader(str, parent: QObject = None)'
    __class__ = QPluginLoader
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, parent: QObject=None):
        'QPluginLoader(parent: QObject = None)\nQPluginLoader(str, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def instance(cls, self):
        'instance(self) -> QObject'
        pass
    
    @classmethod
    def isLoaded(cls, self):
        'isLoaded(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def load(cls, self):
        'load(self) -> bool'
        return True
    
    @classmethod
    def loadHints(cls, self):
        'loadHints(self) -> QLibrary.LoadHints'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setLoadHints(cls, self, UnionQLibraryLoadHints=None, QLibraryLoadHint=None):
        'setLoadHints(self, Union[QLibrary.LoadHints, QLibrary.LoadHint])'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def staticInstances(cls):
        'staticInstances() -> object'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def unload(cls, self):
        'unload(self) -> bool'
        return True
    

class QPoint(_mod_sip.simplewrapper):
    'QPoint()\nQPoint(int, int)\nQPoint(QPoint)'
    def __add__(self, value):
        'Return self+value.'
        return QPoint()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QPoint
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, int, int_):
        'QPoint()\nQPoint(int, int)\nQPoint(QPoint)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QPoint()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return QPoint()
    
    def __pos__(self):
        '+self'
        return QPoint()
    
    def __radd__(self, value):
        'Return value+self.'
        return QPoint()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return QPoint()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QPoint()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QPoint()
    
    def __sub__(self, value):
        'Return self-value.'
        return QPoint()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def dotProduct(cls, QPoint, QPoint_):
        'dotProduct(QPoint, QPoint) -> int'
        return 1
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def manhattanLength(cls, self):
        'manhattanLength(self) -> int'
        return 1
    
    @classmethod
    def setX(cls, self, int):
        'setX(self, int)'
        pass
    
    @classmethod
    def setY(cls, self, int):
        'setY(self, int)'
        pass
    
    @classmethod
    def x(cls, self):
        'x(self) -> int'
        return 1
    
    @classmethod
    def y(cls, self):
        'y(self) -> int'
        return 1
    

class QPointF(_mod_sip.simplewrapper):
    'QPointF()\nQPointF(float, float)\nQPointF(QPoint)\nQPointF(QPointF)'
    def __add__(self, value):
        'Return self+value.'
        return QPointF()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QPointF
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, float, float_):
        'QPointF()\nQPointF(float, float)\nQPointF(QPoint)\nQPointF(QPointF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QPointF()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __neg__(self):
        '-self'
        return QPointF()
    
    def __pos__(self):
        '+self'
        return QPointF()
    
    def __radd__(self, value):
        'Return value+self.'
        return QPointF()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return QPointF()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QPointF()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QPointF()
    
    def __sub__(self, value):
        'Return self-value.'
        return QPointF()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def dotProduct(cls, UnionQPointF=None, QPoint=None, UnionQPointF_=None, QPoint_=None):
        'dotProduct(Union[QPointF, QPoint], Union[QPointF, QPoint]) -> float'
        return 1.0
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def manhattanLength(cls, self):
        'manhattanLength(self) -> float'
        return 1.0
    
    @classmethod
    def setX(cls, self, float):
        'setX(self, float)'
        pass
    
    @classmethod
    def setY(cls, self, float):
        'setY(self, float)'
        pass
    
    @classmethod
    def toPoint(cls, self):
        'toPoint(self) -> QPoint'
        pass
    
    @classmethod
    def x(cls, self):
        'x(self) -> float'
        return 1.0
    
    @classmethod
    def y(cls, self):
        'y(self) -> float'
        return 1.0
    

class QProcess(QIODevice):
    'QProcess(parent: QObject = None)'
    CrashExit = ExitStatus()
    Crashed = ProcessError()
    ExitStatus = ExitStatus
    FailedToStart = ProcessError()
    ForwardedChannels = ProcessChannelMode()
    ForwardedErrorChannel = ProcessChannelMode()
    ForwardedInputChannel = InputChannelMode()
    ForwardedOutputChannel = ProcessChannelMode()
    InputChannelMode = InputChannelMode
    ManagedInputChannel = InputChannelMode()
    MergedChannels = ProcessChannelMode()
    NormalExit = ExitStatus()
    NotRunning = ProcessState()
    ProcessChannel = ProcessChannel
    ProcessChannelMode = ProcessChannelMode
    ProcessError = ProcessError
    ProcessState = ProcessState
    ReadError = ProcessError()
    Running = ProcessState()
    SeparateChannels = ProcessChannelMode()
    StandardError = ProcessChannel()
    StandardOutput = ProcessChannel()
    Starting = ProcessState()
    Timedout = ProcessError()
    UnknownError = ProcessError()
    WriteError = ProcessError()
    __class__ = QProcess
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QProcess(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def arguments(cls, self):
        'arguments(self) -> List[str]'
        pass
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def closeReadChannel(cls, self, QProcessProcessChannel):
        'closeReadChannel(self, QProcess.ProcessChannel)'
        pass
    
    @classmethod
    def closeWriteChannel(cls, self):
        'closeWriteChannel(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    def error(self, QProcessProcessError):
        'error(self) -> QProcess.ProcessError\nerror(self, QProcess.ProcessError) [signal]'
        pass
    
    def errorOccurred(self, QProcessProcessError):
        'errorOccurred(self, QProcess.ProcessError) [signal]'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def execute(cls, str, Iterablestr=None):
        'execute(str, Iterable[str]) -> int\nexecute(str) -> int'
        return 1
    
    @classmethod
    def exitCode(cls, self):
        'exitCode(self) -> int'
        return 1
    
    @classmethod
    def exitStatus(cls, self):
        'exitStatus(self) -> QProcess.ExitStatus'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    def finished(self, int, QProcessExitStatus):
        'finished(self, int, QProcess.ExitStatus) [signal]'
        pass
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def inputChannelMode(cls, self):
        'inputChannelMode(self) -> QProcess.InputChannelMode'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def kill(cls, self):
        'kill(self)'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def nullDevice(cls):
        'nullDevice() -> str'
        return ''
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, mode: Union[QIODevice.OpenMode,QIODevice.OpenModeFlag]=QIODevice.ReadWrite):
        'open(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def pid(cls, self):
        'pid(self) -> sip.voidptr'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def processChannelMode(cls, self):
        'processChannelMode(self) -> QProcess.ProcessChannelMode'
        pass
    
    @classmethod
    def processEnvironment(cls, self):
        'processEnvironment(self) -> QProcessEnvironment'
        pass
    
    @classmethod
    def processId(cls, self):
        'processId(self) -> int'
        return 1
    
    @classmethod
    def program(cls, self):
        'program(self) -> str'
        return ''
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readAllStandardError(cls, self):
        'readAllStandardError(self) -> QByteArray'
        pass
    
    @classmethod
    def readAllStandardOutput(cls, self):
        'readAllStandardOutput(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannel(cls, self):
        'readChannel(self) -> QProcess.ProcessChannel'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls, self, int):
        'readData(self, int) -> bytes'
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls):
        pass
    
    def readyReadStandardError(self):
        'readyReadStandardError(self) [signal]'
        pass
    
    def readyReadStandardOutput(self):
        'readyReadStandardOutput(self) [signal]'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setArguments(cls, self, Iterablestr=None):
        'setArguments(self, Iterable[str])'
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setErrorString(cls):
        pass
    
    @classmethod
    def setInputChannelMode(cls, self, QProcessInputChannelMode):
        'setInputChannelMode(self, QProcess.InputChannelMode)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls):
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProcessChannelMode(cls, self, QProcessProcessChannelMode):
        'setProcessChannelMode(self, QProcess.ProcessChannelMode)'
        pass
    
    @classmethod
    def setProcessEnvironment(cls, self, QProcessEnvironment):
        'setProcessEnvironment(self, QProcessEnvironment)'
        pass
    
    @classmethod
    def setProcessState(cls, self, QProcessProcessState):
        'setProcessState(self, QProcess.ProcessState)'
        pass
    
    @classmethod
    def setProgram(cls, self, str):
        'setProgram(self, str)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setReadChannel(cls, self, QProcessProcessChannel):
        'setReadChannel(self, QProcess.ProcessChannel)'
        pass
    
    @classmethod
    def setStandardErrorFile(cls, self, str, mode: Union[QIODevice.OpenMode,QIODevice.OpenModeFlag]=QIODevice.Truncate):
        'setStandardErrorFile(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate)'
        pass
    
    @classmethod
    def setStandardInputFile(cls, self, str):
        'setStandardInputFile(self, str)'
        pass
    
    @classmethod
    def setStandardOutputFile(cls, self, str, mode: Union[QIODevice.OpenMode,QIODevice.OpenModeFlag]=QIODevice.Truncate):
        'setStandardOutputFile(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.Truncate)'
        pass
    
    @classmethod
    def setStandardOutputProcess(cls, self, QProcess):
        'setStandardOutputProcess(self, QProcess)'
        pass
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def setWorkingDirectory(cls, self, str):
        'setWorkingDirectory(self, str)'
        pass
    
    @classmethod
    def setupChildProcess(cls, self):
        'setupChildProcess(self)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def start(cls, self, str, Iterablestr=None, mode: Union[QIODevice.OpenMode,QIODevice.OpenModeFlag]=QIODevice.ReadWrite):
        'start(self, str, Iterable[str], mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)\nstart(self, str, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)\nstart(self, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)'
        pass
    
    @classmethod
    def startDetached(cls, str, Iterablestr=None, str_=None):
        'startDetached(str, Iterable[str], str) -> Tuple[bool, int]\nstartDetached(str, Iterable[str]) -> bool\nstartDetached(str) -> bool'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    def started(self):
        'started(self) [signal]'
        pass
    
    @classmethod
    def state(cls, self):
        'state(self) -> QProcess.ProcessState'
        pass
    
    def stateChanged(self, QProcessProcessState):
        'stateChanged(self, QProcess.ProcessState) [signal]'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def systemEnvironment(cls):
        'systemEnvironment() -> List[str]'
        pass
    
    @classmethod
    def terminate(cls, self):
        'terminate(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, msecs: int=30000):
        'waitForBytesWritten(self, msecs: int = 30000) -> bool'
        return True
    
    @classmethod
    def waitForFinished(cls, self, msecs: int=30000):
        'waitForFinished(self, msecs: int = 30000) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, msecs: int=30000):
        'waitForReadyRead(self, msecs: int = 30000) -> bool'
        return True
    
    @classmethod
    def waitForStarted(cls, self, msecs: int=30000):
        'waitForStarted(self, msecs: int = 30000) -> bool'
        return True
    
    @classmethod
    def workingDirectory(cls, self):
        'workingDirectory(self) -> str'
        return ''
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls, self, bytes):
        'writeData(self, bytes) -> int'
        return 1
    

class QProcessEnvironment(_mod_sip.simplewrapper):
    'QProcessEnvironment()\nQProcessEnvironment(QProcessEnvironment)'
    __class__ = QProcessEnvironment
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QProcessEnvironment):
        'QProcessEnvironment()\nQProcessEnvironment(QProcessEnvironment)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def contains(cls, self, str):
        'contains(self, str) -> bool'
        return True
    
    @classmethod
    def insert(cls, self, QProcessEnvironment):
        'insert(self, str, str)\ninsert(self, QProcessEnvironment)'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def keys(cls, self):
        'keys(self) -> List[str]'
        pass
    
    @classmethod
    def remove(cls, self, str):
        'remove(self, str)'
        pass
    
    @classmethod
    def swap(cls, self, QProcessEnvironment):
        'swap(self, QProcessEnvironment)'
        pass
    
    @classmethod
    def systemEnvironment(cls):
        'systemEnvironment() -> QProcessEnvironment'
        pass
    
    @classmethod
    def toStringList(cls, self):
        'toStringList(self) -> List[str]'
        pass
    
    @classmethod
    def value(cls, self, str, defaultValue: str=''):
        "value(self, str, defaultValue: str = '') -> str"
        return ''
    

class QPropertyAnimation(QVariantAnimation):
    'QPropertyAnimation(parent: QObject = None)\nQPropertyAnimation(QObject, Union[QByteArray, bytes, bytearray], parent: QObject = None)'
    __class__ = QPropertyAnimation
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QObject, UnionQByteArray=None, bytes=None, bytearray=None, parent: QObject=None):
        'QPropertyAnimation(parent: QObject = None)\nQPropertyAnimation(QObject, Union[QByteArray, bytes, bytearray], parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def currentValue(cls, self):
        'currentValue(self) -> Any'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def easingCurve(cls, self):
        'easingCurve(self) -> QEasingCurve'
        pass
    
    @classmethod
    def endValue(cls, self):
        'endValue(self) -> Any'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def interpolated(cls):
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def keyValueAt(cls, self, float):
        'keyValueAt(self, float) -> Any'
        pass
    
    @classmethod
    def keyValues(cls, self):
        'keyValues(self) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def propertyName(cls, self):
        'propertyName(self) -> QByteArray'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setDuration(cls, self, int):
        'setDuration(self, int)'
        pass
    
    @classmethod
    def setEasingCurve(cls, self, UnionQEasingCurve=None, QEasingCurveType=None):
        'setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type])'
        pass
    
    @classmethod
    def setEndValue(cls, self, Any):
        'setEndValue(self, Any)'
        pass
    
    @classmethod
    def setKeyValueAt(cls, self, float, Any):
        'setKeyValueAt(self, float, Any)'
        pass
    
    @classmethod
    def setKeyValues(cls, self, object):
        'setKeyValues(self, object)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setPropertyName(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'setPropertyName(self, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def setStartValue(cls, self, Any):
        'setStartValue(self, Any)'
        pass
    
    @classmethod
    def setTargetObject(cls, self, QObject):
        'setTargetObject(self, QObject)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startValue(cls, self):
        'startValue(self) -> Any'
        pass
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def targetObject(cls, self):
        'targetObject(self) -> QObject'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls):
        pass
    
    @classmethod
    def updateCurrentValue(cls, self, Any):
        'updateCurrentValue(self, Any)'
        pass
    
    @classmethod
    def updateDirection(cls):
        pass
    
    @classmethod
    def updateState(cls, self, QAbstractAnimationState, QAbstractAnimationState_):
        'updateState(self, QAbstractAnimation.State, QAbstractAnimation.State)'
        pass
    

class QReadLocker(_mod_sip.simplewrapper):
    'QReadLocker(QReadWriteLock)'
    __class__ = QReadLocker
    __dict__ = {}
    @classmethod
    def __enter__(cls, self):
        '__enter__(self) -> object'
        return self
    
    @classmethod
    def __exit__(cls, self, object, object_, object_1):
        '__exit__(self, object, object, object)'
        pass
    
    def __init__(self, QReadWriteLock):
        'QReadLocker(QReadWriteLock)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def readWriteLock(cls, self):
        'readWriteLock(self) -> QReadWriteLock'
        pass
    
    @classmethod
    def relock(cls, self):
        'relock(self)'
        pass
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QReadWriteLock(_mod_sip.simplewrapper):
    'QReadWriteLock(recursionMode: QReadWriteLock.RecursionMode = QReadWriteLock.NonRecursive)'
    NonRecursive = RecursionMode()
    RecursionMode = RecursionMode
    Recursive = RecursionMode()
    __class__ = QReadWriteLock
    __dict__ = {}
    def __init__(self, recursionMode: QReadWriteLock.RecursionMode=QReadWriteLock.NonRecursive):
        'QReadWriteLock(recursionMode: QReadWriteLock.RecursionMode = QReadWriteLock.NonRecursive)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def lockForRead(cls, self):
        'lockForRead(self)'
        pass
    
    @classmethod
    def lockForWrite(cls, self):
        'lockForWrite(self)'
        pass
    
    @classmethod
    def tryLockForRead(cls, self, int):
        'tryLockForRead(self) -> bool\ntryLockForRead(self, int) -> bool'
        return True
    
    @classmethod
    def tryLockForWrite(cls, self, int):
        'tryLockForWrite(self) -> bool\ntryLockForWrite(self, int) -> bool'
        return True
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QRect(_mod_sip.simplewrapper):
    'QRect()\nQRect(int, int, int, int)\nQRect(QPoint, QPoint)\nQRect(QPoint, QSize)\nQRect(QRect)'
    def __add__(self, value):
        'Return self+value.'
        return QRect()
    
    def __and__(self, value):
        'Return self&value.'
        return QRect()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QRect
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __iand__(self, value):
        'Return self&=value.'
        return None
    
    def __init__(self, int, int_, int_1, int_2):
        'QRect()\nQRect(int, int, int, int)\nQRect(QPoint, QPoint)\nQRect(QPoint, QSize)\nQRect(QRect)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __ior__(self, value):
        'Return self|=value.'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __or__(self, value):
        'Return self|value.'
        return QRect()
    
    def __radd__(self, value):
        'Return value+self.'
        return QRect()
    
    def __rand__(self, value):
        'Return value&self.'
        return QRect()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __ror__(self, value):
        'Return value|self.'
        return QRect()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QRect()
    
    def __sub__(self, value):
        'Return self-value.'
        return QRect()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def adjust(cls, self, int, int_, int_1, int_2):
        'adjust(self, int, int, int, int)'
        pass
    
    @classmethod
    def adjusted(cls, self, int, int_, int_1, int_2):
        'adjusted(self, int, int, int, int) -> QRect'
        pass
    
    @classmethod
    def bottom(cls, self):
        'bottom(self) -> int'
        return 1
    
    @classmethod
    def bottomLeft(cls, self):
        'bottomLeft(self) -> QPoint'
        pass
    
    @classmethod
    def bottomRight(cls, self):
        'bottomRight(self) -> QPoint'
        pass
    
    @classmethod
    def center(cls, self):
        'center(self) -> QPoint'
        pass
    
    @classmethod
    def contains(cls, self, QPoint, proper: bool=False):
        'contains(self, QPoint, proper: bool = False) -> bool\ncontains(self, QRect, proper: bool = False) -> bool\ncontains(self, int, int, bool) -> bool\ncontains(self, int, int) -> bool'
        return True
    
    @classmethod
    def getCoords(cls, self):
        'getCoords(self) -> Tuple[int, int, int, int]'
        pass
    
    @classmethod
    def getRect(cls, self):
        'getRect(self) -> Tuple[int, int, int, int]'
        pass
    
    @classmethod
    def height(cls, self):
        'height(self) -> int'
        return 1
    
    @classmethod
    def intersected(cls, self, QRect):
        'intersected(self, QRect) -> QRect'
        pass
    
    @classmethod
    def intersects(cls, self, QRect):
        'intersects(self, QRect) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def left(cls, self):
        'left(self) -> int'
        return 1
    
    @classmethod
    def marginsAdded(cls, self, QMargins):
        'marginsAdded(self, QMargins) -> QRect'
        pass
    
    @classmethod
    def marginsRemoved(cls, self, QMargins):
        'marginsRemoved(self, QMargins) -> QRect'
        pass
    
    @classmethod
    def moveBottom(cls, self, int):
        'moveBottom(self, int)'
        pass
    
    @classmethod
    def moveBottomLeft(cls, self, QPoint):
        'moveBottomLeft(self, QPoint)'
        pass
    
    @classmethod
    def moveBottomRight(cls, self, QPoint):
        'moveBottomRight(self, QPoint)'
        pass
    
    @classmethod
    def moveCenter(cls, self, QPoint):
        'moveCenter(self, QPoint)'
        pass
    
    @classmethod
    def moveLeft(cls, self, int):
        'moveLeft(self, int)'
        pass
    
    @classmethod
    def moveRight(cls, self, int):
        'moveRight(self, int)'
        pass
    
    @classmethod
    def moveTo(cls, self, int, int_):
        'moveTo(self, int, int)\nmoveTo(self, QPoint)'
        pass
    
    @classmethod
    def moveTop(cls, self, int):
        'moveTop(self, int)'
        pass
    
    @classmethod
    def moveTopLeft(cls, self, QPoint):
        'moveTopLeft(self, QPoint)'
        pass
    
    @classmethod
    def moveTopRight(cls, self, QPoint):
        'moveTopRight(self, QPoint)'
        pass
    
    @classmethod
    def normalized(cls, self):
        'normalized(self) -> QRect'
        pass
    
    @classmethod
    def right(cls, self):
        'right(self) -> int'
        return 1
    
    @classmethod
    def setBottom(cls, self, int):
        'setBottom(self, int)'
        pass
    
    @classmethod
    def setBottomLeft(cls, self, QPoint):
        'setBottomLeft(self, QPoint)'
        pass
    
    @classmethod
    def setBottomRight(cls, self, QPoint):
        'setBottomRight(self, QPoint)'
        pass
    
    @classmethod
    def setCoords(cls, self, int, int_, int_1, int_2):
        'setCoords(self, int, int, int, int)'
        pass
    
    @classmethod
    def setHeight(cls, self, int):
        'setHeight(self, int)'
        pass
    
    @classmethod
    def setLeft(cls, self, int):
        'setLeft(self, int)'
        pass
    
    @classmethod
    def setRect(cls, self, int, int_, int_1, int_2):
        'setRect(self, int, int, int, int)'
        pass
    
    @classmethod
    def setRight(cls, self, int):
        'setRight(self, int)'
        pass
    
    @classmethod
    def setSize(cls, self, QSize):
        'setSize(self, QSize)'
        pass
    
    @classmethod
    def setTop(cls, self, int):
        'setTop(self, int)'
        pass
    
    @classmethod
    def setTopLeft(cls, self, QPoint):
        'setTopLeft(self, QPoint)'
        pass
    
    @classmethod
    def setTopRight(cls, self, QPoint):
        'setTopRight(self, QPoint)'
        pass
    
    @classmethod
    def setWidth(cls, self, int):
        'setWidth(self, int)'
        pass
    
    @classmethod
    def setX(cls, self, int):
        'setX(self, int)'
        pass
    
    @classmethod
    def setY(cls, self, int):
        'setY(self, int)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> QSize'
        pass
    
    @classmethod
    def top(cls, self):
        'top(self) -> int'
        return 1
    
    @classmethod
    def topLeft(cls, self):
        'topLeft(self) -> QPoint'
        pass
    
    @classmethod
    def topRight(cls, self):
        'topRight(self) -> QPoint'
        pass
    
    @classmethod
    def translate(cls, self, int, int_):
        'translate(self, int, int)\ntranslate(self, QPoint)'
        pass
    
    @classmethod
    def translated(cls, self, int, int_):
        'translated(self, int, int) -> QRect\ntranslated(self, QPoint) -> QRect'
        pass
    
    @classmethod
    def transposed(cls, self):
        'transposed(self) -> QRect'
        pass
    
    @classmethod
    def united(cls, self, QRect):
        'united(self, QRect) -> QRect'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> int'
        return 1
    
    @classmethod
    def x(cls, self):
        'x(self) -> int'
        return 1
    
    @classmethod
    def y(cls, self):
        'y(self) -> int'
        return 1
    

class QRectF(_mod_sip.simplewrapper):
    'QRectF()\nQRectF(Union[QPointF, QPoint], QSizeF)\nQRectF(Union[QPointF, QPoint], Union[QPointF, QPoint])\nQRectF(float, float, float, float)\nQRectF(QRect)\nQRectF(QRectF)'
    def __add__(self, value):
        'Return self+value.'
        return QRectF()
    
    def __and__(self, value):
        'Return self&value.'
        return QRectF()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QRectF
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __iand__(self, value):
        'Return self&=value.'
        return None
    
    def __init__(self, UnionQPointF=None, QPoint=None, UnionQPointF_=None, QPoint_=None):
        'QRectF()\nQRectF(Union[QPointF, QPoint], QSizeF)\nQRectF(Union[QPointF, QPoint], Union[QPointF, QPoint])\nQRectF(float, float, float, float)\nQRectF(QRect)\nQRectF(QRectF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __ior__(self, value):
        'Return self|=value.'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __or__(self, value):
        'Return self|value.'
        return QRectF()
    
    def __radd__(self, value):
        'Return value+self.'
        return QRectF()
    
    def __rand__(self, value):
        'Return value&self.'
        return QRectF()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __ror__(self, value):
        'Return value|self.'
        return QRectF()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QRectF()
    
    def __sub__(self, value):
        'Return self-value.'
        return QRectF()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def adjust(cls, self, float, float_, float_1, float_2):
        'adjust(self, float, float, float, float)'
        pass
    
    @classmethod
    def adjusted(cls, self, float, float_, float_1, float_2):
        'adjusted(self, float, float, float, float) -> QRectF'
        pass
    
    @classmethod
    def bottom(cls, self):
        'bottom(self) -> float'
        return 1.0
    
    @classmethod
    def bottomLeft(cls, self):
        'bottomLeft(self) -> QPointF'
        pass
    
    @classmethod
    def bottomRight(cls, self):
        'bottomRight(self) -> QPointF'
        pass
    
    @classmethod
    def center(cls, self):
        'center(self) -> QPointF'
        pass
    
    @classmethod
    def contains(cls, self, UnionQPointF=None, QPoint=None):
        'contains(self, Union[QPointF, QPoint]) -> bool\ncontains(self, QRectF) -> bool\ncontains(self, float, float) -> bool'
        return True
    
    @classmethod
    def getCoords(cls, self):
        'getCoords(self) -> Tuple[float, float, float, float]'
        pass
    
    @classmethod
    def getRect(cls, self):
        'getRect(self) -> Tuple[float, float, float, float]'
        pass
    
    @classmethod
    def height(cls, self):
        'height(self) -> float'
        return 1.0
    
    @classmethod
    def intersected(cls, self, QRectF):
        'intersected(self, QRectF) -> QRectF'
        pass
    
    @classmethod
    def intersects(cls, self, QRectF):
        'intersects(self, QRectF) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def left(cls, self):
        'left(self) -> float'
        return 1.0
    
    @classmethod
    def marginsAdded(cls, self, QMarginsF):
        'marginsAdded(self, QMarginsF) -> QRectF'
        pass
    
    @classmethod
    def marginsRemoved(cls, self, QMarginsF):
        'marginsRemoved(self, QMarginsF) -> QRectF'
        pass
    
    @classmethod
    def moveBottom(cls, self, float):
        'moveBottom(self, float)'
        pass
    
    @classmethod
    def moveBottomLeft(cls, self, UnionQPointF=None, QPoint=None):
        'moveBottomLeft(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def moveBottomRight(cls, self, UnionQPointF=None, QPoint=None):
        'moveBottomRight(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def moveCenter(cls, self, UnionQPointF=None, QPoint=None):
        'moveCenter(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def moveLeft(cls, self, float):
        'moveLeft(self, float)'
        pass
    
    @classmethod
    def moveRight(cls, self, float):
        'moveRight(self, float)'
        pass
    
    @classmethod
    def moveTo(cls, self, UnionQPointF=None, QPoint=None):
        'moveTo(self, float, float)\nmoveTo(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def moveTop(cls, self, float):
        'moveTop(self, float)'
        pass
    
    @classmethod
    def moveTopLeft(cls, self, UnionQPointF=None, QPoint=None):
        'moveTopLeft(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def moveTopRight(cls, self, UnionQPointF=None, QPoint=None):
        'moveTopRight(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def normalized(cls, self):
        'normalized(self) -> QRectF'
        pass
    
    @classmethod
    def right(cls, self):
        'right(self) -> float'
        return 1.0
    
    @classmethod
    def setBottom(cls, self, float):
        'setBottom(self, float)'
        pass
    
    @classmethod
    def setBottomLeft(cls, self, UnionQPointF=None, QPoint=None):
        'setBottomLeft(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setBottomRight(cls, self, UnionQPointF=None, QPoint=None):
        'setBottomRight(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setCoords(cls, self, float, float_, float_1, float_2):
        'setCoords(self, float, float, float, float)'
        pass
    
    @classmethod
    def setHeight(cls, self, float):
        'setHeight(self, float)'
        pass
    
    @classmethod
    def setLeft(cls, self, float):
        'setLeft(self, float)'
        pass
    
    @classmethod
    def setRect(cls, self, float, float_, float_1, float_2):
        'setRect(self, float, float, float, float)'
        pass
    
    @classmethod
    def setRight(cls, self, float):
        'setRight(self, float)'
        pass
    
    @classmethod
    def setSize(cls, self, QSizeF):
        'setSize(self, QSizeF)'
        pass
    
    @classmethod
    def setTop(cls, self, float):
        'setTop(self, float)'
        pass
    
    @classmethod
    def setTopLeft(cls, self, UnionQPointF=None, QPoint=None):
        'setTopLeft(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setTopRight(cls, self, UnionQPointF=None, QPoint=None):
        'setTopRight(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def setWidth(cls, self, float):
        'setWidth(self, float)'
        pass
    
    @classmethod
    def setX(cls, self, float):
        'setX(self, float)'
        pass
    
    @classmethod
    def setY(cls, self, float):
        'setY(self, float)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> QSizeF'
        pass
    
    @classmethod
    def toAlignedRect(cls, self):
        'toAlignedRect(self) -> QRect'
        pass
    
    @classmethod
    def toRect(cls, self):
        'toRect(self) -> QRect'
        pass
    
    @classmethod
    def top(cls, self):
        'top(self) -> float'
        return 1.0
    
    @classmethod
    def topLeft(cls, self):
        'topLeft(self) -> QPointF'
        pass
    
    @classmethod
    def topRight(cls, self):
        'topRight(self) -> QPointF'
        pass
    
    @classmethod
    def translate(cls, self, UnionQPointF=None, QPoint=None):
        'translate(self, float, float)\ntranslate(self, Union[QPointF, QPoint])'
        pass
    
    @classmethod
    def translated(cls, self, UnionQPointF=None, QPoint=None):
        'translated(self, float, float) -> QRectF\ntranslated(self, Union[QPointF, QPoint]) -> QRectF'
        pass
    
    @classmethod
    def transposed(cls, self):
        'transposed(self) -> QRectF'
        pass
    
    @classmethod
    def united(cls, self, QRectF):
        'united(self, QRectF) -> QRectF'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> float'
        return 1.0
    
    @classmethod
    def x(cls, self):
        'x(self) -> float'
        return 1.0
    
    @classmethod
    def y(cls, self):
        'y(self) -> float'
        return 1.0
    

class QRegExp(_mod_sip.simplewrapper):
    'QRegExp()\nQRegExp(str, cs: Qt.CaseSensitivity = Qt.CaseSensitive, syntax: QRegExp.PatternSyntax = QRegExp.RegExp)\nQRegExp(QRegExp)'
    CaretAtOffset = CaretMode()
    CaretAtZero = CaretMode()
    CaretMode = CaretMode
    CaretWontMatch = CaretMode()
    FixedString = PatternSyntax()
    PatternSyntax = PatternSyntax
    RegExp = PatternSyntax()
    RegExp2 = PatternSyntax()
    W3CXmlSchema11 = PatternSyntax()
    Wildcard = PatternSyntax()
    WildcardUnix = PatternSyntax()
    __class__ = QRegExp
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, str, cs: Qt.CaseSensitivity=Qt.CaseSensitive, syntax: QRegExp.PatternSyntax=QRegExp.RegExp):
        'QRegExp()\nQRegExp(str, cs: Qt.CaseSensitivity = Qt.CaseSensitive, syntax: QRegExp.PatternSyntax = QRegExp.RegExp)\nQRegExp(QRegExp)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def cap(cls, self, nth: int=0):
        'cap(self, nth: int = 0) -> str'
        return ''
    
    @classmethod
    def captureCount(cls, self):
        'captureCount(self) -> int'
        return 1
    
    @classmethod
    def capturedTexts(cls, self):
        'capturedTexts(self) -> List[str]'
        pass
    
    @classmethod
    def caseSensitivity(cls, self):
        'caseSensitivity(self) -> Qt.CaseSensitivity'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def escape(cls, str):
        'escape(str) -> str'
        return ''
    
    @classmethod
    def exactMatch(cls, self, str):
        'exactMatch(self, str) -> bool'
        return True
    
    @classmethod
    def indexIn(cls, self, str, offset: int=0, caretMode: QRegExp.CaretMode=QRegExp.CaretAtZero):
        'indexIn(self, str, offset: int = 0, caretMode: QRegExp.CaretMode = QRegExp.CaretAtZero) -> int'
        return 1
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isMinimal(cls, self):
        'isMinimal(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def lastIndexIn(cls, self, str, offset: int=-1, caretMode: QRegExp.CaretMode=QRegExp.CaretAtZero):
        'lastIndexIn(self, str, offset: int = -1, caretMode: QRegExp.CaretMode = QRegExp.CaretAtZero) -> int'
        return 1
    
    @classmethod
    def matchedLength(cls, self):
        'matchedLength(self) -> int'
        return 1
    
    @classmethod
    def pattern(cls, self):
        'pattern(self) -> str'
        return ''
    
    @classmethod
    def patternSyntax(cls, self):
        'patternSyntax(self) -> QRegExp.PatternSyntax'
        pass
    
    @classmethod
    def pos(cls, self, nth: int=0):
        'pos(self, nth: int = 0) -> int'
        return 1
    
    @classmethod
    def setCaseSensitivity(cls, self, QtCaseSensitivity):
        'setCaseSensitivity(self, Qt.CaseSensitivity)'
        pass
    
    @classmethod
    def setMinimal(cls, self, bool):
        'setMinimal(self, bool)'
        pass
    
    @classmethod
    def setPattern(cls, self, str):
        'setPattern(self, str)'
        pass
    
    @classmethod
    def setPatternSyntax(cls, self, QRegExpPatternSyntax):
        'setPatternSyntax(self, QRegExp.PatternSyntax)'
        pass
    
    @classmethod
    def swap(cls, self, QRegExp):
        'swap(self, QRegExp)'
        pass
    

class QRegularExpression(_mod_sip.simplewrapper):
    'QRegularExpression()\nQRegularExpression(str, options: Union[QRegularExpression.PatternOptions, QRegularExpression.PatternOption] = QRegularExpression.NoPatternOption)\nQRegularExpression(QRegularExpression)'
    AnchoredMatchOption = MatchOption()
    CaseInsensitiveOption = PatternOption()
    DontAutomaticallyOptimizeOption = PatternOption()
    DontCaptureOption = PatternOption()
    DontCheckSubjectStringMatchOption = MatchOption()
    DotMatchesEverythingOption = PatternOption()
    ExtendedPatternSyntaxOption = PatternOption()
    InvertedGreedinessOption = PatternOption()
    MatchOption = MatchOption
    MatchOptions = MatchOptions
    MatchType = MatchType
    MultilineOption = PatternOption()
    NoMatch = MatchType()
    NoMatchOption = MatchOption()
    NoPatternOption = PatternOption()
    NormalMatch = MatchType()
    OptimizeOnFirstUsageOption = PatternOption()
    PartialPreferCompleteMatch = MatchType()
    PartialPreferFirstMatch = MatchType()
    PatternOption = PatternOption
    PatternOptions = PatternOptions
    UseUnicodePropertiesOption = PatternOption()
    __class__ = QRegularExpression
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, str, options: Union[QRegularExpression.PatternOptions,QRegularExpression.PatternOption]=QRegularExpression.NoPatternOption):
        'QRegularExpression()\nQRegularExpression(str, options: Union[QRegularExpression.PatternOptions, QRegularExpression.PatternOption] = QRegularExpression.NoPatternOption)\nQRegularExpression(QRegularExpression)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def captureCount(cls, self):
        'captureCount(self) -> int'
        return 1
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def escape(cls, str):
        'escape(str) -> str'
        return ''
    
    @classmethod
    def globalMatch(cls, self, str, offset: int=0, matchType: QRegularExpression.MatchType=QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions,QRegularExpression.MatchOption]=QRegularExpression.NoMatchOption):
        'globalMatch(self, str, offset: int = 0, matchType: QRegularExpression.MatchType = QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions, QRegularExpression.MatchOption] = QRegularExpression.NoMatchOption) -> QRegularExpressionMatchIterator'
        pass
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def match(cls, self, str, offset: int=0, matchType: QRegularExpression.MatchType=QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions,QRegularExpression.MatchOption]=QRegularExpression.NoMatchOption):
        'match(self, str, offset: int = 0, matchType: QRegularExpression.MatchType = QRegularExpression.NormalMatch, matchOptions: Union[QRegularExpression.MatchOptions, QRegularExpression.MatchOption] = QRegularExpression.NoMatchOption) -> QRegularExpressionMatch'
        pass
    
    @classmethod
    def namedCaptureGroups(cls, self):
        'namedCaptureGroups(self) -> List[str]'
        pass
    
    @classmethod
    def optimize(cls, self):
        'optimize(self)'
        pass
    
    @classmethod
    def pattern(cls, self):
        'pattern(self) -> str'
        return ''
    
    @classmethod
    def patternErrorOffset(cls, self):
        'patternErrorOffset(self) -> int'
        return 1
    
    @classmethod
    def patternOptions(cls, self):
        'patternOptions(self) -> QRegularExpression.PatternOptions'
        pass
    
    @classmethod
    def setPattern(cls, self, str):
        'setPattern(self, str)'
        pass
    
    @classmethod
    def setPatternOptions(cls, self, UnionQRegularExpressionPatternOptions=None, QRegularExpressionPatternOption=None):
        'setPatternOptions(self, Union[QRegularExpression.PatternOptions, QRegularExpression.PatternOption])'
        pass
    
    @classmethod
    def swap(cls, self, QRegularExpression):
        'swap(self, QRegularExpression)'
        pass
    

class QRegularExpressionMatch(_mod_sip.simplewrapper):
    'QRegularExpressionMatch()\nQRegularExpressionMatch(QRegularExpressionMatch)'
    __class__ = QRegularExpressionMatch
    __dict__ = {}
    def __init__(self, QRegularExpressionMatch):
        'QRegularExpressionMatch()\nQRegularExpressionMatch(QRegularExpressionMatch)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def captured(cls, self, nth: int=0):
        'captured(self, nth: int = 0) -> str\ncaptured(self, str) -> str'
        return ''
    
    @classmethod
    def capturedEnd(cls, self, nth: int=0):
        'capturedEnd(self, nth: int = 0) -> int\ncapturedEnd(self, str) -> int'
        return 1
    
    @classmethod
    def capturedLength(cls, self, nth: int=0):
        'capturedLength(self, nth: int = 0) -> int\ncapturedLength(self, str) -> int'
        return 1
    
    @classmethod
    def capturedStart(cls, self, nth: int=0):
        'capturedStart(self, nth: int = 0) -> int\ncapturedStart(self, str) -> int'
        return 1
    
    @classmethod
    def capturedTexts(cls, self):
        'capturedTexts(self) -> List[str]'
        pass
    
    @classmethod
    def hasMatch(cls, self):
        'hasMatch(self) -> bool'
        return True
    
    @classmethod
    def hasPartialMatch(cls, self):
        'hasPartialMatch(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def lastCapturedIndex(cls, self):
        'lastCapturedIndex(self) -> int'
        return 1
    
    @classmethod
    def matchOptions(cls, self):
        'matchOptions(self) -> QRegularExpression.MatchOptions'
        pass
    
    @classmethod
    def matchType(cls, self):
        'matchType(self) -> QRegularExpression.MatchType'
        pass
    
    @classmethod
    def regularExpression(cls, self):
        'regularExpression(self) -> QRegularExpression'
        pass
    
    @classmethod
    def swap(cls, self, QRegularExpressionMatch):
        'swap(self, QRegularExpressionMatch)'
        pass
    

class QRegularExpressionMatchIterator(_mod_sip.simplewrapper):
    'QRegularExpressionMatchIterator()\nQRegularExpressionMatchIterator(QRegularExpressionMatchIterator)'
    __class__ = QRegularExpressionMatchIterator
    __dict__ = {}
    def __init__(self, QRegularExpressionMatchIterator):
        'QRegularExpressionMatchIterator()\nQRegularExpressionMatchIterator(QRegularExpressionMatchIterator)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def hasNext(cls, self):
        'hasNext(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def matchOptions(cls, self):
        'matchOptions(self) -> QRegularExpression.MatchOptions'
        pass
    
    @classmethod
    def matchType(cls, self):
        'matchType(self) -> QRegularExpression.MatchType'
        pass
    
    @classmethod
    def next(cls, self):
        'next(self) -> QRegularExpressionMatch'
        pass
    
    @classmethod
    def peekNext(cls, self):
        'peekNext(self) -> QRegularExpressionMatch'
        pass
    
    @classmethod
    def regularExpression(cls, self):
        'regularExpression(self) -> QRegularExpression'
        pass
    
    @classmethod
    def swap(cls, self, QRegularExpressionMatchIterator):
        'swap(self, QRegularExpressionMatchIterator)'
        pass
    

class QResource(_mod_sip.simplewrapper):
    "QResource(fileName: str = '', locale: QLocale = QLocale())"
    __class__ = QResource
    __dict__ = {}
    def __init__(self, fileName: str='', locale: QLocale=QLocale()):
        "QResource(fileName: str = '', locale: QLocale = QLocale())"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def absoluteFilePath(cls, self):
        'absoluteFilePath(self) -> str'
        return ''
    
    @classmethod
    def children(cls, self):
        'children(self) -> List[str]'
        pass
    
    @classmethod
    def data(cls, self):
        'data(self) -> bytes'
        pass
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def isCompressed(cls, self):
        'isCompressed(self) -> bool'
        return True
    
    @classmethod
    def isDir(cls, self):
        'isDir(self) -> bool'
        return True
    
    @classmethod
    def isFile(cls, self):
        'isFile(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def lastModified(cls, self):
        'lastModified(self) -> QDateTime'
        pass
    
    @classmethod
    def locale(cls, self):
        'locale(self) -> QLocale'
        pass
    
    @classmethod
    def registerResource(cls, str, mapRoot: str=''):
        "registerResource(str, mapRoot: str = '') -> bool"
        return True
    
    @classmethod
    def registerResourceData(cls, bytes, mapRoot: str=''):
        "registerResourceData(bytes, mapRoot: str = '') -> bool"
        return True
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setLocale(cls, self, QLocale):
        'setLocale(self, QLocale)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def unregisterResource(cls, str, mapRoot: str=''):
        "unregisterResource(str, mapRoot: str = '') -> bool"
        return True
    
    @classmethod
    def unregisterResourceData(cls, bytes, mapRoot: str=''):
        "unregisterResourceData(bytes, mapRoot: str = '') -> bool"
        return True
    

class QRunnable(_mod_sip.wrapper):
    'QRunnable()\nQRunnable(QRunnable)'
    __class__ = QRunnable
    __dict__ = {}
    def __init__(self, QRunnable):
        'QRunnable()\nQRunnable(QRunnable)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def autoDelete(cls, self):
        'autoDelete(self) -> bool'
        return True
    
    @classmethod
    def run(cls, self):
        'run(self)'
        pass
    
    @classmethod
    def setAutoDelete(cls, self, bool):
        'setAutoDelete(self, bool)'
        pass
    

class QSaveFile(QFileDevice):
    'QSaveFile(str)\nQSaveFile(parent: QObject = None)\nQSaveFile(str, QObject)'
    __class__ = QSaveFile
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QSaveFile(str)\nQSaveFile(parent: QObject = None)\nQSaveFile(str, QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def cancelWriting(cls, self):
        'cancelWriting(self)'
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls):
        pass
    
    @classmethod
    def commit(cls, self):
        'commit(self) -> bool'
        return True
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def directWriteFallback(cls, self):
        'directWriteFallback(self) -> bool'
        return True
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QFileDevice.FileError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls, self):
        'flush(self) -> bool'
        return True
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def handle(cls, self):
        'handle(self) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def map(cls, self, int, int_, flags: QFileDevice.MemoryMapFlags=QFileDevice.NoOptions):
        'map(self, int, int, flags: QFileDevice.MemoryMapFlags = QFileDevice.NoOptions) -> sip.voidptr'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, UnionQIODeviceOpenMode=None, QIODeviceOpenModeFlag=None):
        'open(self, Union[QIODevice.OpenMode, QIODevice.OpenModeFlag]) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def permissions(cls, self):
        'permissions(self) -> QFileDevice.Permissions'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls):
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls):
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setDirectWriteFallback(cls, self, bool):
        'setDirectWriteFallback(self, bool)'
        pass
    
    @classmethod
    def setErrorString(cls):
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls):
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPermissions(cls, self, UnionQFileDevicePermissions=None, QFileDevicePermission=None):
        'setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool'
        return True
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def unmap(cls, self, sipvoidptr):
        'unmap(self, sip.voidptr) -> bool'
        return True
    
    @classmethod
    def unsetError(cls, self):
        'unsetError(self)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls, self, bytes):
        'writeData(self, bytes) -> int'
        return 1
    

class QSemaphore(_mod_sip.simplewrapper):
    'QSemaphore(n: int = 0)'
    __class__ = QSemaphore
    __dict__ = {}
    def __init__(self, n: int=0):
        'QSemaphore(n: int = 0)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def acquire(cls, self, n: int=1):
        'acquire(self, n: int = 1)'
        pass
    
    @classmethod
    def available(cls, self):
        'available(self) -> int'
        return 1
    
    @classmethod
    def release(cls, self, n: int=1):
        'release(self, n: int = 1)'
        pass
    
    @classmethod
    def tryAcquire(cls, self, n: int=1):
        'tryAcquire(self, n: int = 1) -> bool\ntryAcquire(self, int, int) -> bool'
        return True
    

class QSequentialAnimationGroup(QAnimationGroup):
    'QSequentialAnimationGroup(parent: QObject = None)'
    __class__ = QSequentialAnimationGroup
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QSequentialAnimationGroup(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def addPause(cls, self, int):
        'addPause(self, int) -> QPauseAnimation'
        pass
    
    @classmethod
    def animationAt(cls, self, int):
        'animationAt(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def animationCount(cls, self):
        'animationCount(self) -> int'
        return 1
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentAnimation(cls, self):
        'currentAnimation(self) -> QAbstractAnimation'
        pass
    
    def currentAnimationChanged(self, QAbstractAnimation):
        'currentAnimationChanged(self, QAbstractAnimation) [signal]'
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def indexOfAnimation(cls, self, QAbstractAnimation):
        'indexOfAnimation(self, QAbstractAnimation) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertAnimation(cls, self, int, QAbstractAnimation):
        'insertAnimation(self, int, QAbstractAnimation)'
        pass
    
    @classmethod
    def insertPause(cls, self, int, int_):
        'insertPause(self, int, int) -> QPauseAnimation'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def takeAnimation(cls, self, int):
        'takeAnimation(self, int) -> QAbstractAnimation'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls, self, int):
        'updateCurrentTime(self, int)'
        pass
    
    @classmethod
    def updateDirection(cls, self, QAbstractAnimationDirection):
        'updateDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def updateState(cls, self, QAbstractAnimationState, QAbstractAnimationState_):
        'updateState(self, QAbstractAnimation.State, QAbstractAnimation.State)'
        pass
    

class QSettings(QObject):
    "QSettings(str, application: str = '', parent: QObject = None)\nQSettings(QSettings.Scope, str, application: str = '', parent: QObject = None)\nQSettings(QSettings.Format, QSettings.Scope, str, application: str = '', parent: QObject = None)\nQSettings(str, QSettings.Format, parent: QObject = None)\nQSettings(parent: QObject = None)"
    AccessError = Status()
    Format = Format
    FormatError = Status()
    IniFormat = Format()
    InvalidFormat = Format()
    NativeFormat = Format()
    NoError = Status()
    Scope = Scope
    Status = Status
    SystemScope = Scope()
    UserScope = Scope()
    __class__ = QSettings
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QSettingsFormat, QSettingsScope, str, application: str='', parent: QObject=None):
        "QSettings(str, application: str = '', parent: QObject = None)\nQSettings(QSettings.Scope, str, application: str = '', parent: QObject = None)\nQSettings(QSettings.Format, QSettings.Scope, str, application: str = '', parent: QObject = None)\nQSettings(str, QSettings.Format, parent: QObject = None)\nQSettings(parent: QObject = None)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def allKeys(cls, self):
        'allKeys(self) -> List[str]'
        pass
    
    @classmethod
    def applicationName(cls, self):
        'applicationName(self) -> str'
        return ''
    
    @classmethod
    def beginGroup(cls, self, str):
        'beginGroup(self, str)'
        pass
    
    @classmethod
    def beginReadArray(cls, self, str):
        'beginReadArray(self, str) -> int'
        return 1
    
    @classmethod
    def beginWriteArray(cls, self, str, size: int=-1):
        'beginWriteArray(self, str, size: int = -1)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def childGroups(cls, self):
        'childGroups(self) -> List[str]'
        pass
    
    @classmethod
    def childKeys(cls, self):
        'childKeys(self) -> List[str]'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def contains(cls, self, str):
        'contains(self, str) -> bool'
        return True
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def defaultFormat(cls):
        'defaultFormat() -> QSettings.Format'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def endArray(cls, self):
        'endArray(self)'
        pass
    
    @classmethod
    def endGroup(cls, self):
        'endGroup(self)'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fallbacksEnabled(cls, self):
        'fallbacksEnabled(self) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def format(cls, self):
        'format(self) -> QSettings.Format'
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> str'
        return ''
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def iniCodec(cls, self):
        'iniCodec(self) -> QTextCodec'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def organizationName(cls, self):
        'organizationName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def remove(cls, self, str):
        'remove(self, str)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def scope(cls, self):
        'scope(self) -> QSettings.Scope'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setArrayIndex(cls, self, int):
        'setArrayIndex(self, int)'
        pass
    
    @classmethod
    def setDefaultFormat(cls, QSettingsFormat):
        'setDefaultFormat(QSettings.Format)'
        pass
    
    @classmethod
    def setFallbacksEnabled(cls, self, bool):
        'setFallbacksEnabled(self, bool)'
        pass
    
    @classmethod
    def setIniCodec(cls, self, QTextCodec):
        'setIniCodec(self, QTextCodec)\nsetIniCodec(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPath(cls, QSettingsFormat, QSettingsScope, str):
        'setPath(QSettings.Format, QSettings.Scope, str)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setValue(cls, self, str, Any):
        'setValue(self, str, Any)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def status(cls, self):
        'status(self) -> QSettings.Status'
        pass
    
    @classmethod
    def sync(cls, self):
        'sync(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def value(cls, self, str, defaultValue: Any=None, type: type=None):
        'value(self, str, defaultValue: Any = None, type: type = None) -> object'
        pass
    

class QSharedMemory(QObject):
    'QSharedMemory(parent: QObject = None)\nQSharedMemory(str, parent: QObject = None)'
    AccessMode = AccessMode
    AlreadyExists = SharedMemoryError()
    InvalidSize = SharedMemoryError()
    KeyError = SharedMemoryError()
    LockError = SharedMemoryError()
    NoError = SharedMemoryError()
    NotFound = SharedMemoryError()
    OutOfResources = SharedMemoryError()
    PermissionDenied = SharedMemoryError()
    ReadOnly = AccessMode()
    ReadWrite = AccessMode()
    SharedMemoryError = SharedMemoryError
    UnknownError = SharedMemoryError()
    __class__ = QSharedMemory
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, parent: QObject=None):
        'QSharedMemory(parent: QObject = None)\nQSharedMemory(str, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def attach(cls, self, mode: QSharedMemory.AccessMode=QSharedMemory.ReadWrite):
        'attach(self, mode: QSharedMemory.AccessMode = QSharedMemory.ReadWrite) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def constData(cls, self):
        'constData(self) -> sip.voidptr'
        pass
    
    @classmethod
    def create(cls, self, int, mode: QSharedMemory.AccessMode=QSharedMemory.ReadWrite):
        'create(self, int, mode: QSharedMemory.AccessMode = QSharedMemory.ReadWrite) -> bool'
        return True
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self):
        'data(self) -> sip.voidptr'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def detach(cls, self):
        'detach(self) -> bool'
        return True
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QSharedMemory.SharedMemoryError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isAttached(cls, self):
        'isAttached(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def key(cls, self):
        'key(self) -> str'
        return ''
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def lock(cls, self):
        'lock(self) -> bool'
        return True
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def nativeKey(cls, self):
        'nativeKey(self) -> str'
        return ''
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setKey(cls, self, str):
        'setKey(self, str)'
        pass
    
    @classmethod
    def setNativeKey(cls, self, str):
        'setNativeKey(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def unlock(cls, self):
        'unlock(self) -> bool'
        return True
    

class QSignalBlocker(_mod_sip.simplewrapper):
    'QSignalBlocker(QObject)'
    __class__ = QSignalBlocker
    __dict__ = {}
    @classmethod
    def __enter__(cls, self):
        '__enter__(self) -> object'
        return self
    
    @classmethod
    def __exit__(cls, self, object, object_, object_1):
        '__exit__(self, object, object, object)'
        pass
    
    def __init__(self, QObject):
        'QSignalBlocker(QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def reblock(cls, self):
        'reblock(self)'
        pass
    
    @classmethod
    def unblock(cls, self):
        'unblock(self)'
        pass
    

class QSignalMapper(QObject):
    'QSignalMapper(parent: QObject = None)'
    __class__ = QSignalMapper
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QSignalMapper(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def map(cls, self, QObject):
        'map(self)\nmap(self, QObject)'
        pass
    
    def mapped(self, QObject):
        'mapped(self, int) [signal]\nmapped(self, str) [signal]\nmapped(self, QObject) [signal]'
        pass
    
    @classmethod
    def mapping(cls, self, QObject):
        'mapping(self, int) -> QObject\nmapping(self, str) -> QObject\nmapping(self, QWidget) -> QObject\nmapping(self, QObject) -> QObject'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeMappings(cls, self, QObject):
        'removeMappings(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setMapping(cls, self, QObject, QObject_):
        'setMapping(self, QObject, int)\nsetMapping(self, QObject, str)\nsetMapping(self, QObject, QWidget)\nsetMapping(self, QObject, QObject)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QSignalTransition(QAbstractTransition):
    'QSignalTransition(sourceState: QState = None)\nQSignalTransition(pyqtBoundSignal, sourceState: QState = None)'
    __class__ = QSignalTransition
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, pyqtBoundSignal, sourceState: QState=None):
        'QSignalTransition(sourceState: QState = None)\nQSignalTransition(pyqtBoundSignal, sourceState: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def addAnimation(cls, self, QAbstractAnimation):
        'addAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def animations(cls, self):
        'animations(self) -> object'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def eventTest(cls, self, QEvent):
        'eventTest(self, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onTransition(cls, self, QEvent):
        'onTransition(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeAnimation(cls, self, QAbstractAnimation):
        'removeAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderObject(cls, self):
        'senderObject(self) -> QObject'
        pass
    
    def senderObjectChanged(self):
        'senderObjectChanged(self) [signal]'
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setSenderObject(cls, self, QObject):
        'setSenderObject(self, QObject)'
        pass
    
    @classmethod
    def setSignal(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'setSignal(self, Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def setTargetState(cls, self, QAbstractState):
        'setTargetState(self, QAbstractState)'
        pass
    
    @classmethod
    def setTargetStates(cls, self, IterableQAbstractState=None):
        'setTargetStates(self, Iterable[QAbstractState])'
        pass
    
    @classmethod
    def setTransitionType(cls, self, QAbstractTransitionTransitionType):
        'setTransitionType(self, QAbstractTransition.TransitionType)'
        pass
    
    @classmethod
    def signal(cls, self):
        'signal(self) -> QByteArray'
        pass
    
    def signalChanged(self):
        'signalChanged(self) [signal]'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sourceState(cls, self):
        'sourceState(self) -> QState'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def targetState(cls, self):
        'targetState(self) -> QAbstractState'
        pass
    
    @classmethod
    def targetStates(cls, self):
        'targetStates(self) -> object'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transitionType(cls, self):
        'transitionType(self) -> QAbstractTransition.TransitionType'
        pass
    

class QSize(_mod_sip.simplewrapper):
    'QSize()\nQSize(int, int)\nQSize(QSize)'
    def __add__(self, value):
        'Return self+value.'
        return QSize()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QSize
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, int, int_):
        'QSize()\nQSize(int, int)\nQSize(QSize)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QSize()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QSize()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return QSize()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QSize()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QSize()
    
    def __sub__(self, value):
        'Return self-value.'
        return QSize()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def boundedTo(cls, self, QSize):
        'boundedTo(self, QSize) -> QSize'
        pass
    
    @classmethod
    def expandedTo(cls, self, QSize):
        'expandedTo(self, QSize) -> QSize'
        pass
    
    @classmethod
    def height(cls, self):
        'height(self) -> int'
        return 1
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def scale(cls, self, int, int_, QtAspectRatioMode):
        'scale(self, QSize, Qt.AspectRatioMode)\nscale(self, int, int, Qt.AspectRatioMode)'
        pass
    
    @classmethod
    def scaled(cls, self, int, int_, QtAspectRatioMode):
        'scaled(self, QSize, Qt.AspectRatioMode) -> QSize\nscaled(self, int, int, Qt.AspectRatioMode) -> QSize'
        pass
    
    @classmethod
    def setHeight(cls, self, int):
        'setHeight(self, int)'
        pass
    
    @classmethod
    def setWidth(cls, self, int):
        'setWidth(self, int)'
        pass
    
    @classmethod
    def transpose(cls, self):
        'transpose(self)'
        pass
    
    @classmethod
    def transposed(cls, self):
        'transposed(self) -> QSize'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> int'
        return 1
    

class QSizeF(_mod_sip.simplewrapper):
    'QSizeF()\nQSizeF(QSize)\nQSizeF(float, float)\nQSizeF(QSizeF)'
    def __add__(self, value):
        'Return self+value.'
        return QSizeF()
    
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QSizeF
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Return self+=value.'
        return None
    
    def __imul__(self, value):
        'Return self*=value.'
        return None
    
    def __init__(self, float, float_):
        'QSizeF()\nQSizeF(QSize)\nQSizeF(float, float)\nQSizeF(QSizeF)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __isub__(self, value):
        'Return self-=value.'
        return None
    
    def __itruediv__(self, value):
        'Return self/=value.'
        pass
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __mul__(self, value):
        'Return self*value.'
        return QSizeF()
    
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __radd__(self, value):
        'Return value+self.'
        return QSizeF()
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    def __rmul__(self, value):
        'Return value*self.'
        return QSizeF()
    
    def __rsub__(self, value):
        'Return value-self.'
        return QSizeF()
    
    def __rtruediv__(self, value):
        'Return value/self.'
        return QSizeF()
    
    def __sub__(self, value):
        'Return self-value.'
        return QSizeF()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def __truediv__(self, value):
        'Return self/value.'
        return 0.0
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def boundedTo(cls, self, QSizeF):
        'boundedTo(self, QSizeF) -> QSizeF'
        pass
    
    @classmethod
    def expandedTo(cls, self, QSizeF):
        'expandedTo(self, QSizeF) -> QSizeF'
        pass
    
    @classmethod
    def height(cls, self):
        'height(self) -> float'
        return 1.0
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def scale(cls, self, float, float_, QtAspectRatioMode):
        'scale(self, QSizeF, Qt.AspectRatioMode)\nscale(self, float, float, Qt.AspectRatioMode)'
        pass
    
    @classmethod
    def scaled(cls, self, float, float_, QtAspectRatioMode):
        'scaled(self, QSizeF, Qt.AspectRatioMode) -> QSizeF\nscaled(self, float, float, Qt.AspectRatioMode) -> QSizeF'
        pass
    
    @classmethod
    def setHeight(cls, self, float):
        'setHeight(self, float)'
        pass
    
    @classmethod
    def setWidth(cls, self, float):
        'setWidth(self, float)'
        pass
    
    @classmethod
    def toSize(cls, self):
        'toSize(self) -> QSize'
        pass
    
    @classmethod
    def transpose(cls, self):
        'transpose(self)'
        pass
    
    @classmethod
    def transposed(cls, self):
        'transposed(self) -> QSizeF'
        pass
    
    @classmethod
    def width(cls, self):
        'width(self) -> float'
        return 1.0
    

class QSocketNotifier(QObject):
    'QSocketNotifier(sip.voidptr, QSocketNotifier.Type, parent: QObject = None)'
    Exception = Type()
    Read = Type()
    Type = Type
    Write = Type()
    __class__ = QSocketNotifier
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, sipvoidptr, QSocketNotifierType, parent: QObject=None):
        'QSocketNotifier(sip.voidptr, QSocketNotifier.Type, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def activated(self, int):
        'activated(self, int) [signal]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isEnabled(cls, self):
        'isEnabled(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setEnabled(cls, self, bool):
        'setEnabled(self, bool)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def socket(cls, self):
        'socket(self) -> sip.voidptr'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def type(cls, self):
        'type(self) -> QSocketNotifier.Type'
        pass
    

class QSortFilterProxyModel(QAbstractProxyModel):
    'QSortFilterProxyModel(parent: QObject = None)'
    __class__ = QSortFilterProxyModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QSortFilterProxyModel(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls, self, parent: QModelIndex=QModelIndex()):
        'columnCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, role: int=Qt.DisplayRole):
        'data(self, QModelIndex, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def dynamicSortFilter(cls, self):
        'dynamicSortFilter(self) -> bool'
        return True
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def filterAcceptsColumn(cls, self, int, QModelIndex):
        'filterAcceptsColumn(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def filterAcceptsRow(cls, self, int, QModelIndex):
        'filterAcceptsRow(self, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def filterCaseSensitivity(cls, self):
        'filterCaseSensitivity(self) -> Qt.CaseSensitivity'
        pass
    
    @classmethod
    def filterKeyColumn(cls, self):
        'filterKeyColumn(self) -> int'
        return 1
    
    @classmethod
    def filterRegExp(cls, self):
        'filterRegExp(self) -> QRegExp'
        pass
    
    @classmethod
    def filterRole(cls, self):
        'filterRole(self) -> int'
        return 1
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls, self, parent: QModelIndex=QModelIndex()):
        'hasChildren(self, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'index(self, int, int, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def invalidate(cls, self):
        'invalidate(self)'
        pass
    
    @classmethod
    def invalidateFilter(cls, self):
        'invalidateFilter(self)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isSortLocaleAware(cls, self):
        'isSortLocaleAware(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> Dict[int, Any]'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def lessThan(cls, self, QModelIndex, QModelIndex_):
        'lessThan(self, QModelIndex, QModelIndex) -> bool'
        return True
    
    @classmethod
    def mapFromSource(cls, self, QModelIndex):
        'mapFromSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def mapSelectionFromSource(cls, self, QItemSelection):
        'mapSelectionFromSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapSelectionToSource(cls, self, QItemSelection):
        'mapSelectionToSource(self, QItemSelection) -> QItemSelection'
        pass
    
    @classmethod
    def mapToSource(cls, self, QModelIndex):
        'mapToSource(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self, QModelIndex):
        'parent(self, QModelIndex) -> QModelIndex\nparent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls):
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setDynamicSortFilter(cls, self, bool):
        'setDynamicSortFilter(self, bool)'
        pass
    
    @classmethod
    def setFilterCaseSensitivity(cls, self, QtCaseSensitivity):
        'setFilterCaseSensitivity(self, Qt.CaseSensitivity)'
        pass
    
    @classmethod
    def setFilterFixedString(cls, self, str):
        'setFilterFixedString(self, str)'
        pass
    
    @classmethod
    def setFilterKeyColumn(cls, self, int):
        'setFilterKeyColumn(self, int)'
        pass
    
    @classmethod
    def setFilterRegExp(cls, self, QRegExp):
        'setFilterRegExp(self, QRegExp)\nsetFilterRegExp(self, str)'
        pass
    
    @classmethod
    def setFilterRole(cls, self, int):
        'setFilterRole(self, int)'
        pass
    
    @classmethod
    def setFilterWildcard(cls, self, str):
        'setFilterWildcard(self, str)'
        pass
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setSortCaseSensitivity(cls, self, QtCaseSensitivity):
        'setSortCaseSensitivity(self, Qt.CaseSensitivity)'
        pass
    
    @classmethod
    def setSortLocaleAware(cls, self, bool):
        'setSortLocaleAware(self, bool)'
        pass
    
    @classmethod
    def setSortRole(cls, self, int):
        'setSortRole(self, int)'
        pass
    
    @classmethod
    def setSourceModel(cls, self, QAbstractItemModel):
        'setSourceModel(self, QAbstractItemModel)'
        pass
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def sortCaseSensitivity(cls, self):
        'sortCaseSensitivity(self) -> Qt.CaseSensitivity'
        pass
    
    @classmethod
    def sortColumn(cls, self):
        'sortColumn(self) -> int'
        return 1
    
    @classmethod
    def sortOrder(cls, self):
        'sortOrder(self) -> Qt.SortOrder'
        pass
    
    @classmethod
    def sortRole(cls, self):
        'sortRole(self) -> int'
        return 1
    
    @classmethod
    def sourceModel(cls, self):
        'sourceModel(self) -> QAbstractItemModel'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QStandardPaths(_mod_sip.simplewrapper):
    'QStandardPaths(QStandardPaths)'
    AppConfigLocation = StandardLocation()
    AppDataLocation = StandardLocation()
    AppLocalDataLocation = StandardLocation()
    ApplicationsLocation = StandardLocation()
    CacheLocation = StandardLocation()
    ConfigLocation = StandardLocation()
    DataLocation = StandardLocation()
    DesktopLocation = StandardLocation()
    DocumentsLocation = StandardLocation()
    DownloadLocation = StandardLocation()
    FontsLocation = StandardLocation()
    GenericCacheLocation = StandardLocation()
    GenericConfigLocation = StandardLocation()
    GenericDataLocation = StandardLocation()
    HomeLocation = StandardLocation()
    LocateDirectory = LocateOption()
    LocateFile = LocateOption()
    LocateOption = LocateOption
    LocateOptions = LocateOptions
    MoviesLocation = StandardLocation()
    MusicLocation = StandardLocation()
    PicturesLocation = StandardLocation()
    RuntimeLocation = StandardLocation()
    StandardLocation = StandardLocation
    TempLocation = StandardLocation()
    __class__ = QStandardPaths
    __dict__ = {}
    def __init__(self, QStandardPaths):
        'QStandardPaths(QStandardPaths)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def displayName(cls, QStandardPathsStandardLocation):
        'displayName(QStandardPaths.StandardLocation) -> str'
        return ''
    
    @classmethod
    def enableTestMode(cls, bool):
        'enableTestMode(bool)'
        pass
    
    @classmethod
    def findExecutable(cls, str, paths: Iterable[str]=[]):
        'findExecutable(str, paths: Iterable[str] = []) -> str'
        return ''
    
    @classmethod
    def locate(cls, QStandardPathsStandardLocation, str, options: QStandardPaths.LocateOptions=QStandardPaths.LocateFile):
        'locate(QStandardPaths.StandardLocation, str, options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> str'
        return ''
    
    @classmethod
    def locateAll(cls, QStandardPathsStandardLocation, str, options: QStandardPaths.LocateOptions=QStandardPaths.LocateFile):
        'locateAll(QStandardPaths.StandardLocation, str, options: QStandardPaths.LocateOptions = QStandardPaths.LocateFile) -> List[str]'
        pass
    
    @classmethod
    def setTestModeEnabled(cls, bool):
        'setTestModeEnabled(bool)'
        pass
    
    @classmethod
    def standardLocations(cls, QStandardPathsStandardLocation):
        'standardLocations(QStandardPaths.StandardLocation) -> List[str]'
        pass
    
    @classmethod
    def writableLocation(cls, QStandardPathsStandardLocation):
        'writableLocation(QStandardPaths.StandardLocation) -> str'
        return ''
    

class QState(QAbstractState):
    'QState(parent: QState = None)\nQState(QState.ChildMode, parent: QState = None)'
    ChildMode = ChildMode
    DontRestoreProperties = RestorePolicy()
    ExclusiveStates = ChildMode()
    ParallelStates = ChildMode()
    RestorePolicy = RestorePolicy
    RestoreProperties = RestorePolicy()
    __class__ = QState
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QStateChildMode, parent: QState=None):
        'QState(parent: QState = None)\nQState(QState.ChildMode, parent: QState = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def active(cls, self):
        'active(self) -> bool'
        return True
    
    @classmethod
    def addTransition(cls, self, pyqtBoundSignal, QAbstractState):
        'addTransition(self, QAbstractTransition)\naddTransition(self, pyqtBoundSignal, QAbstractState) -> QSignalTransition\naddTransition(self, QAbstractState) -> QAbstractTransition'
        pass
    
    @classmethod
    def assignProperty(cls, self, QObject, str, Any):
        'assignProperty(self, QObject, str, Any)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def childMode(cls, self):
        'childMode(self) -> QState.ChildMode'
        pass
    
    def childModeChanged(self):
        'childModeChanged(self) [signal]'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def errorState(cls, self):
        'errorState(self) -> QAbstractState'
        pass
    
    def errorStateChanged(self):
        'errorStateChanged(self) [signal]'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    def finished(self):
        'finished(self) [signal]'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def initialState(cls, self):
        'initialState(self) -> QAbstractState'
        pass
    
    def initialStateChanged(self):
        'initialStateChanged(self) [signal]'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onEntry(cls, self, QEvent):
        'onEntry(self, QEvent)'
        pass
    
    @classmethod
    def onExit(cls, self, QEvent):
        'onExit(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentState(cls, self):
        'parentState(self) -> QState'
        pass
    
    def propertiesAssigned(self):
        'propertiesAssigned(self) [signal]'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeTransition(cls, self, QAbstractTransition):
        'removeTransition(self, QAbstractTransition)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setChildMode(cls, self, QStateChildMode):
        'setChildMode(self, QState.ChildMode)'
        pass
    
    @classmethod
    def setErrorState(cls, self, QAbstractState):
        'setErrorState(self, QAbstractState)'
        pass
    
    @classmethod
    def setInitialState(cls, self, QAbstractState):
        'setInitialState(self, QAbstractState)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transitions(cls, self):
        'transitions(self) -> object'
        pass
    

class QStateMachine(QState):
    'QStateMachine(parent: QObject = None)\nQStateMachine(QState.ChildMode, parent: QObject = None)'
    Error = Error
    EventPriority = EventPriority
    HighPriority = EventPriority()
    NoCommonAncestorForTransitionError = Error()
    NoDefaultStateInHistoryStateError = Error()
    NoError = Error()
    NoInitialStateError = Error()
    NormalPriority = EventPriority()
    SignalEvent = SignalEvent
    WrappedEvent = WrappedEvent
    __class__ = QStateMachine
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, QStateChildMode, parent: QObject=None):
        'QStateMachine(parent: QObject = None)\nQStateMachine(QState.ChildMode, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def active(cls, self):
        'active(self) -> bool'
        return True
    
    @classmethod
    def addDefaultAnimation(cls, self, QAbstractAnimation):
        'addDefaultAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def addState(cls, self, QAbstractState):
        'addState(self, QAbstractState)'
        pass
    
    @classmethod
    def addTransition(cls, self, pyqtBoundSignal, QAbstractState):
        'addTransition(self, QAbstractTransition)\naddTransition(self, pyqtBoundSignal, QAbstractState) -> QSignalTransition\naddTransition(self, QAbstractState) -> QAbstractTransition'
        pass
    
    @classmethod
    def assignProperty(cls, self, QObject, str, Any):
        'assignProperty(self, QObject, str, Any)'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def cancelDelayedEvent(cls, self, int):
        'cancelDelayedEvent(self, int) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def childMode(cls, self):
        'childMode(self) -> QState.ChildMode'
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clearError(cls, self):
        'clearError(self)'
        pass
    
    @classmethod
    def configuration(cls, self):
        'configuration(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def defaultAnimations(cls, self):
        'defaultAnimations(self) -> List[QAbstractAnimation]'
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QStateMachine.Error'
        pass
    
    @classmethod
    def errorState(cls, self):
        'errorState(self) -> QAbstractState'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def globalRestorePolicy(cls, self):
        'globalRestorePolicy(self) -> QState.RestorePolicy'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def initialState(cls, self):
        'initialState(self) -> QAbstractState'
        pass
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isAnimated(cls, self):
        'isAnimated(self) -> bool'
        return True
    
    @classmethod
    def isRunning(cls, self):
        'isRunning(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def machine(cls, self):
        'machine(self) -> QStateMachine'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def onEntry(cls, self, QEvent):
        'onEntry(self, QEvent)'
        pass
    
    @classmethod
    def onExit(cls, self, QEvent):
        'onExit(self, QEvent)'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def parentState(cls, self):
        'parentState(self) -> QState'
        pass
    
    @classmethod
    def postDelayedEvent(cls, self, QEvent, int):
        'postDelayedEvent(self, QEvent, int) -> int'
        return 1
    
    @classmethod
    def postEvent(cls, self, QEvent, priority: QStateMachine.EventPriority=QStateMachine.NormalPriority):
        'postEvent(self, QEvent, priority: QStateMachine.EventPriority = QStateMachine.NormalPriority)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeDefaultAnimation(cls, self, QAbstractAnimation):
        'removeDefaultAnimation(self, QAbstractAnimation)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeState(cls, self, QAbstractState):
        'removeState(self, QAbstractState)'
        pass
    
    @classmethod
    def removeTransition(cls, self, QAbstractTransition):
        'removeTransition(self, QAbstractTransition)'
        pass
    
    def runningChanged(self, bool):
        'runningChanged(self, bool) [signal]'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setAnimated(cls, self, bool):
        'setAnimated(self, bool)'
        pass
    
    @classmethod
    def setChildMode(cls, self, QStateChildMode):
        'setChildMode(self, QState.ChildMode)'
        pass
    
    @classmethod
    def setErrorState(cls, self, QAbstractState):
        'setErrorState(self, QAbstractState)'
        pass
    
    @classmethod
    def setGlobalRestorePolicy(cls, self, QStateRestorePolicy):
        'setGlobalRestorePolicy(self, QState.RestorePolicy)'
        pass
    
    @classmethod
    def setInitialState(cls, self, QAbstractState):
        'setInitialState(self, QAbstractState)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setRunning(cls, self, bool):
        'setRunning(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self):
        'start(self)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    def started(self):
        'started(self) [signal]'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    def stopped(self):
        'stopped(self) [signal]'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def transitions(cls, self):
        'transitions(self) -> object'
        pass
    

class QStorageInfo(_mod_sip.simplewrapper):
    'QStorageInfo()\nQStorageInfo(str)\nQStorageInfo(QDir)\nQStorageInfo(QStorageInfo)'
    __class__ = QStorageInfo
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QStorageInfo):
        'QStorageInfo()\nQStorageInfo(str)\nQStorageInfo(QDir)\nQStorageInfo(QStorageInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def blockSize(cls, self):
        'blockSize(self) -> int'
        return 1
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesFree(cls, self):
        'bytesFree(self) -> int'
        return 1
    
    @classmethod
    def bytesTotal(cls, self):
        'bytesTotal(self) -> int'
        return 1
    
    @classmethod
    def device(cls, self):
        'device(self) -> QByteArray'
        pass
    
    @classmethod
    def displayName(cls, self):
        'displayName(self) -> str'
        return ''
    
    @classmethod
    def fileSystemType(cls, self):
        'fileSystemType(self) -> QByteArray'
        pass
    
    @classmethod
    def isReadOnly(cls, self):
        'isReadOnly(self) -> bool'
        return True
    
    @classmethod
    def isReady(cls, self):
        'isReady(self) -> bool'
        return True
    
    @classmethod
    def isRoot(cls, self):
        'isRoot(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def mountedVolumes(cls):
        'mountedVolumes() -> object'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def refresh(cls, self):
        'refresh(self)'
        pass
    
    @classmethod
    def root(cls):
        'root() -> QStorageInfo'
        pass
    
    @classmethod
    def rootPath(cls, self):
        'rootPath(self) -> str'
        return ''
    
    @classmethod
    def setPath(cls, self, str):
        'setPath(self, str)'
        pass
    
    @classmethod
    def subvolume(cls, self):
        'subvolume(self) -> QByteArray'
        pass
    
    @classmethod
    def swap(cls, self, QStorageInfo):
        'swap(self, QStorageInfo)'
        pass
    

class QStringListModel(QAbstractListModel):
    'QStringListModel(parent: QObject = None)\nQStringListModel(Iterable[str], parent: QObject = None)'
    __class__ = QStringListModel
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, Iterablestr=None, parent: QObject=None):
        'QStringListModel(parent: QObject = None)\nQStringListModel(Iterable[str], parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def beginInsertColumns(cls):
        pass
    
    @classmethod
    def beginInsertRows(cls):
        pass
    
    @classmethod
    def beginMoveColumns(cls):
        pass
    
    @classmethod
    def beginMoveRows(cls):
        pass
    
    @classmethod
    def beginRemoveColumns(cls):
        pass
    
    @classmethod
    def beginRemoveRows(cls):
        pass
    
    @classmethod
    def beginResetModel(cls):
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def buddy(cls, self, QModelIndex):
        'buddy(self, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def canDropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'canDropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def canFetchMore(cls, self, QModelIndex):
        'canFetchMore(self, QModelIndex) -> bool'
        return True
    
    @classmethod
    def changePersistentIndex(cls):
        pass
    
    @classmethod
    def changePersistentIndexList(cls):
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def columnCount(cls):
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def createIndex(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def data(cls, self, QModelIndex, int):
        'data(self, QModelIndex, int) -> Any'
        pass
    
    @classmethod
    def decodeData(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dropMimeData(cls, self, QMimeData, QtDropAction, int, int_, QModelIndex):
        'dropMimeData(self, QMimeData, Qt.DropAction, int, int, QModelIndex) -> bool'
        return True
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeData(cls):
        pass
    
    @classmethod
    def endInsertColumns(cls):
        pass
    
    @classmethod
    def endInsertRows(cls):
        pass
    
    @classmethod
    def endMoveColumns(cls):
        pass
    
    @classmethod
    def endMoveRows(cls):
        pass
    
    @classmethod
    def endRemoveColumns(cls):
        pass
    
    @classmethod
    def endRemoveRows(cls):
        pass
    
    @classmethod
    def endResetModel(cls):
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def fetchMore(cls, self, QModelIndex):
        'fetchMore(self, QModelIndex)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flags(cls, self, QModelIndex):
        'flags(self, QModelIndex) -> Qt.ItemFlags'
        pass
    
    @classmethod
    def hasChildren(cls):
        pass
    
    @classmethod
    def hasIndex(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'hasIndex(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def headerData(cls, self, int, QtOrientation, role: int=Qt.DisplayRole):
        'headerData(self, int, Qt.Orientation, role: int = Qt.DisplayRole) -> Any'
        pass
    
    @classmethod
    def index(cls, self, int, column: int=0, parent: QModelIndex=QModelIndex()):
        'index(self, int, column: int = 0, parent: QModelIndex = QModelIndex()) -> QModelIndex'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def insertColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'insertRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def insertRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'insertRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def itemData(cls, self, QModelIndex):
        'itemData(self, QModelIndex) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def match(cls, self, QModelIndex, int, Any, hits: int=1, flags: Union[Qt.MatchFlags,Qt.MatchFlag]=Qt.MatchStartsWith|Qt.MatchWrap):
        'match(self, QModelIndex, int, Any, hits: int = 1, flags: Union[Qt.MatchFlags, Qt.MatchFlag] = Qt.MatchStartsWith|Qt.MatchWrap) -> object'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def mimeData(cls, self, object):
        'mimeData(self, object) -> QMimeData'
        pass
    
    @classmethod
    def mimeTypes(cls, self):
        'mimeTypes(self) -> List[str]'
        pass
    
    @classmethod
    def moveColumn(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveColumn(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveColumns(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveColumns(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRow(cls, self, QModelIndex, int, QModelIndex_, int_):
        'moveRow(self, QModelIndex, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveRows(cls, self, QModelIndex, int, int_, QModelIndex_, int_1):
        'moveRows(self, QModelIndex, int, int, QModelIndex, int) -> bool'
        return True
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def persistentIndexList(cls):
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeColumn(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeColumn(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeColumns(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeColumns(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def removeRow(cls, self, int, parent: QModelIndex=QModelIndex()):
        'removeRow(self, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def removeRows(cls, self, int, int_, parent: QModelIndex=QModelIndex()):
        'removeRows(self, int, int, parent: QModelIndex = QModelIndex()) -> bool'
        return True
    
    @classmethod
    def resetInternalData(cls):
        pass
    
    @classmethod
    def revert(cls, self):
        'revert(self)'
        pass
    
    @classmethod
    def roleNames(cls, self):
        'roleNames(self) -> object'
        pass
    
    @classmethod
    def rowCount(cls, self, parent: QModelIndex=QModelIndex()):
        'rowCount(self, parent: QModelIndex = QModelIndex()) -> int'
        return 1
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setData(cls, self, QModelIndex, Any, role: int=Qt.EditRole):
        'setData(self, QModelIndex, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setHeaderData(cls, self, int, QtOrientation, Any, role: int=Qt.EditRole):
        'setHeaderData(self, int, Qt.Orientation, Any, role: int = Qt.EditRole) -> bool'
        return True
    
    @classmethod
    def setItemData(cls, self, QModelIndex, Dictint=None, Any=None):
        'setItemData(self, QModelIndex, Dict[int, Any]) -> bool'
        return True
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setStringList(cls, self, Iterablestr=None):
        'setStringList(self, Iterable[str])'
        pass
    
    @classmethod
    def sibling(cls, self, int, int_, QModelIndex):
        'sibling(self, int, int, QModelIndex) -> QModelIndex'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sort(cls, self, int, order: Qt.SortOrder=Qt.AscendingOrder):
        'sort(self, int, order: Qt.SortOrder = Qt.AscendingOrder)'
        pass
    
    @classmethod
    def span(cls, self, QModelIndex):
        'span(self, QModelIndex) -> QSize'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stringList(cls, self):
        'stringList(self) -> List[str]'
        pass
    
    @classmethod
    def submit(cls, self):
        'submit(self) -> bool'
        return True
    
    @classmethod
    def supportedDragActions(cls, self):
        'supportedDragActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def supportedDropActions(cls, self):
        'supportedDropActions(self) -> Qt.DropActions'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QSysInfo(_mod_sip.simplewrapper):
    'QSysInfo()\nQSysInfo(QSysInfo)'
    BigEndian = Endian()
    ByteOrder = Endian()
    Endian = Endian
    LittleEndian = Endian()
    Sizes = Sizes
    WV_10_0 = WinVersion()
    WV_2000 = WinVersion()
    WV_2003 = WinVersion()
    WV_32s = WinVersion()
    WV_4_0 = WinVersion()
    WV_5_0 = WinVersion()
    WV_5_1 = WinVersion()
    WV_5_2 = WinVersion()
    WV_6_0 = WinVersion()
    WV_6_1 = WinVersion()
    WV_6_2 = WinVersion()
    WV_6_3 = WinVersion()
    WV_95 = WinVersion()
    WV_98 = WinVersion()
    WV_CE = WinVersion()
    WV_CENET = WinVersion()
    WV_CE_5 = WinVersion()
    WV_CE_6 = WinVersion()
    WV_CE_based = WinVersion()
    WV_DOS_based = WinVersion()
    WV_Me = WinVersion()
    WV_NT = WinVersion()
    WV_NT_based = WinVersion()
    WV_VISTA = WinVersion()
    WV_WINDOWS10 = WinVersion()
    WV_WINDOWS7 = WinVersion()
    WV_WINDOWS8 = WinVersion()
    WV_WINDOWS8_1 = WinVersion()
    WV_XP = WinVersion()
    WinVersion = WinVersion
    WindowsVersion = WinVersion()
    WordSize = Sizes()
    __class__ = QSysInfo
    __dict__ = {}
    def __init__(self, QSysInfo):
        'QSysInfo()\nQSysInfo(QSysInfo)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def buildAbi(cls):
        'buildAbi() -> str'
        return ''
    
    @classmethod
    def buildCpuArchitecture(cls):
        'buildCpuArchitecture() -> str'
        return ''
    
    @classmethod
    def currentCpuArchitecture(cls):
        'currentCpuArchitecture() -> str'
        return ''
    
    @classmethod
    def kernelType(cls):
        'kernelType() -> str'
        return ''
    
    @classmethod
    def kernelVersion(cls):
        'kernelVersion() -> str'
        return ''
    
    @classmethod
    def machineHostName(cls):
        'machineHostName() -> str'
        return ''
    
    @classmethod
    def prettyProductName(cls):
        'prettyProductName() -> str'
        return ''
    
    @classmethod
    def productType(cls):
        'productType() -> str'
        return ''
    
    @classmethod
    def productVersion(cls):
        'productVersion() -> str'
        return ''
    
    @classmethod
    def windowsVersion(cls):
        'windowsVersion() -> QSysInfo.WinVersion'
        pass
    

class QSystemSemaphore(_mod_sip.simplewrapper):
    'QSystemSemaphore(str, initialValue: int = 0, mode: QSystemSemaphore.AccessMode = QSystemSemaphore.Open)'
    AccessMode = AccessMode
    AlreadyExists = SystemSemaphoreError()
    Create = AccessMode()
    KeyError = SystemSemaphoreError()
    NoError = SystemSemaphoreError()
    NotFound = SystemSemaphoreError()
    Open = AccessMode()
    OutOfResources = SystemSemaphoreError()
    PermissionDenied = SystemSemaphoreError()
    SystemSemaphoreError = SystemSemaphoreError
    UnknownError = SystemSemaphoreError()
    __class__ = QSystemSemaphore
    __dict__ = {}
    def __init__(self, str, initialValue: int=0, mode: QSystemSemaphore.AccessMode=QSystemSemaphore.Open):
        'QSystemSemaphore(str, initialValue: int = 0, mode: QSystemSemaphore.AccessMode = QSystemSemaphore.Open)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def acquire(cls, self):
        'acquire(self) -> bool'
        return True
    
    @classmethod
    def error(cls, self):
        'error(self) -> QSystemSemaphore.SystemSemaphoreError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def key(cls, self):
        'key(self) -> str'
        return ''
    
    @classmethod
    def release(cls, self, n: int=1):
        'release(self, n: int = 1) -> bool'
        return True
    
    @classmethod
    def setKey(cls, self, str, initialValue: int=0, mode: QSystemSemaphore.AccessMode=QSystemSemaphore.Open):
        'setKey(self, str, initialValue: int = 0, mode: QSystemSemaphore.AccessMode = QSystemSemaphore.Open)'
        pass
    

def QT_TRANSLATE_NOOP(str, str_):
    'QT_TRANSLATE_NOOP(str, str) -> str'
    return ''

def QT_TR_NOOP(str):
    'QT_TR_NOOP(str) -> str'
    return ''

def QT_TR_NOOP_UTF8(str):
    'QT_TR_NOOP_UTF8(str) -> str'
    return ''

QT_VERSION = 329990
QT_VERSION_STR = '5.9.6'
class QTemporaryDir(_mod_sip.simplewrapper):
    'QTemporaryDir()\nQTemporaryDir(str)'
    __class__ = QTemporaryDir
    __dict__ = {}
    def __init__(self, str):
        'QTemporaryDir()\nQTemporaryDir(str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def autoRemove(cls, self):
        'autoRemove(self) -> bool'
        return True
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def filePath(cls, self, str):
        'filePath(self, str) -> str'
        return ''
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def path(cls, self):
        'path(self) -> str'
        return ''
    
    @classmethod
    def remove(cls, self):
        'remove(self) -> bool'
        return True
    
    @classmethod
    def setAutoRemove(cls, self, bool):
        'setAutoRemove(self, bool)'
        pass
    

class QTemporaryFile(QFile):
    'QTemporaryFile()\nQTemporaryFile(str)\nQTemporaryFile(QObject)\nQTemporaryFile(str, QObject)'
    __class__ = QTemporaryFile
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, str, QObject):
        'QTemporaryFile()\nQTemporaryFile(str)\nQTemporaryFile(QObject)\nQTemporaryFile(str, QObject)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def autoRemove(cls, self):
        'autoRemove(self) -> bool'
        return True
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def bytesAvailable(cls, self):
        'bytesAvailable(self) -> int'
        return 1
    
    @classmethod
    def bytesToWrite(cls, self):
        'bytesToWrite(self) -> int'
        return 1
    
    @classmethod
    def canReadLine(cls, self):
        'canReadLine(self) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def close(cls, self):
        'close(self)'
        pass
    
    @classmethod
    def commitTransaction(cls, self):
        'commitTransaction(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def copy(cls, self, str):
        'copy(self, str) -> bool\ncopy(str, str) -> bool'
        return True
    
    @classmethod
    def createNativeFile(cls, QFile):
        'createNativeFile(str) -> QTemporaryFile\ncreateNativeFile(QFile) -> QTemporaryFile'
        pass
    
    @classmethod
    def currentReadChannel(cls, self):
        'currentReadChannel(self) -> int'
        return 1
    
    @classmethod
    def currentWriteChannel(cls, self):
        'currentWriteChannel(self) -> int'
        return 1
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def decodeName(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'decodeName(Union[QByteArray, bytes, bytearray]) -> str\ndecodeName(str) -> str'
        return ''
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def encodeName(cls, str):
        'encodeName(str) -> QByteArray'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QFileDevice.FileError'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def exists(cls, self):
        'exists(self) -> bool\nexists(str) -> bool'
        return True
    
    @classmethod
    def fileName(cls, self):
        'fileName(self) -> str'
        return ''
    
    @classmethod
    def fileTemplate(cls, self):
        'fileTemplate(self) -> str'
        return ''
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def flush(cls, self):
        'flush(self) -> bool'
        return True
    
    @classmethod
    def getChar(cls, self):
        'getChar(self) -> Tuple[bool, str]'
        pass
    
    @classmethod
    def handle(cls, self):
        'handle(self) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isOpen(cls, self):
        'isOpen(self) -> bool'
        return True
    
    @classmethod
    def isReadable(cls, self):
        'isReadable(self) -> bool'
        return True
    
    @classmethod
    def isSequential(cls, self):
        'isSequential(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isTextModeEnabled(cls, self):
        'isTextModeEnabled(self) -> bool'
        return True
    
    @classmethod
    def isTransactionStarted(cls, self):
        'isTransactionStarted(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def isWritable(cls, self):
        'isWritable(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def link(cls, self, str):
        'link(self, str) -> bool\nlink(str, str) -> bool'
        return True
    
    @classmethod
    def map(cls, self, int, int_, flags: QFileDevice.MemoryMapFlags=QFileDevice.NoOptions):
        'map(self, int, int, flags: QFileDevice.MemoryMapFlags = QFileDevice.NoOptions) -> sip.voidptr'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def open(cls, self, QIODeviceOpenMode):
        'open(self) -> bool\nopen(self, QIODevice.OpenMode) -> bool'
        return True
    
    @classmethod
    def openMode(cls, self):
        'openMode(self) -> QIODevice.OpenMode'
        pass
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def peek(cls, self, int):
        'peek(self, int) -> QByteArray'
        pass
    
    @classmethod
    def permissions(cls, self):
        'permissions(self) -> QFileDevice.Permissions\npermissions(str) -> QFileDevice.Permissions'
        pass
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def putChar(cls, self, str):
        'putChar(self, str) -> bool'
        return True
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> bytes'
        pass
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> QByteArray'
        pass
    
    @classmethod
    def readChannelCount(cls, self):
        'readChannelCount(self) -> int'
        return 1
    
    @classmethod
    def readData(cls):
        pass
    
    @classmethod
    def readLine(cls, self, maxlen: int=0):
        'readLine(self, maxlen: int = 0) -> bytes'
        pass
    
    @classmethod
    def readLineData(cls):
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def remove(cls, self):
        'remove(self) -> bool\nremove(str) -> bool'
        return True
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def rename(cls, self, str):
        'rename(self, str) -> bool\nrename(str, str) -> bool'
        return True
    
    @classmethod
    def reset(cls, self):
        'reset(self) -> bool'
        return True
    
    @classmethod
    def resize(cls, self, int):
        'resize(self, int) -> bool\nresize(str, int) -> bool'
        return True
    
    @classmethod
    def rollbackTransaction(cls, self):
        'rollbackTransaction(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setAutoRemove(cls, self, bool):
        'setAutoRemove(self, bool)'
        pass
    
    @classmethod
    def setCurrentReadChannel(cls, self, int):
        'setCurrentReadChannel(self, int)'
        pass
    
    @classmethod
    def setCurrentWriteChannel(cls, self, int):
        'setCurrentWriteChannel(self, int)'
        pass
    
    @classmethod
    def setErrorString(cls):
        pass
    
    @classmethod
    def setFileName(cls, self, str):
        'setFileName(self, str)'
        pass
    
    @classmethod
    def setFileTemplate(cls, self, str):
        'setFileTemplate(self, str)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setOpenMode(cls):
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPermissions(cls, self, UnionQFileDevicePermissions=None, QFileDevicePermission=None):
        'setPermissions(self, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool\nsetPermissions(str, Union[QFileDevice.Permissions, QFileDevice.Permission]) -> bool'
        return True
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setTextModeEnabled(cls, self, bool):
        'setTextModeEnabled(self, bool)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startTransaction(cls, self):
        'startTransaction(self)'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def symLinkTarget(cls, self):
        'symLinkTarget(self) -> str\nsymLinkTarget(str) -> str'
        return ''
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def ungetChar(cls, self, str):
        'ungetChar(self, str)'
        pass
    
    @classmethod
    def unmap(cls, self, sipvoidptr):
        'unmap(self, sip.voidptr) -> bool'
        return True
    
    @classmethod
    def unsetError(cls, self):
        'unsetError(self)'
        pass
    
    @classmethod
    def waitForBytesWritten(cls, self, int):
        'waitForBytesWritten(self, int) -> bool'
        return True
    
    @classmethod
    def waitForReadyRead(cls, self, int):
        'waitForReadyRead(self, int) -> bool'
        return True
    
    @classmethod
    def write(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'write(self, Union[QByteArray, bytes, bytearray]) -> int'
        return 1
    
    @classmethod
    def writeChannelCount(cls, self):
        'writeChannelCount(self) -> int'
        return 1
    
    @classmethod
    def writeData(cls):
        pass
    

class QTextBoundaryFinder(_mod_sip.simplewrapper):
    'QTextBoundaryFinder()\nQTextBoundaryFinder(QTextBoundaryFinder)\nQTextBoundaryFinder(QTextBoundaryFinder.BoundaryType, str)'
    BoundaryReason = BoundaryReason
    BoundaryReasons = BoundaryReasons
    BoundaryType = BoundaryType
    BreakOpportunity = BoundaryReason()
    EndOfItem = BoundaryReason()
    Grapheme = BoundaryType()
    Line = BoundaryType()
    MandatoryBreak = BoundaryReason()
    NotAtBoundary = BoundaryReason()
    Sentence = BoundaryType()
    SoftHyphen = BoundaryReason()
    StartOfItem = BoundaryReason()
    Word = BoundaryType()
    __class__ = QTextBoundaryFinder
    __dict__ = {}
    def __init__(self, QTextBoundaryFinderBoundaryType, str):
        'QTextBoundaryFinder()\nQTextBoundaryFinder(QTextBoundaryFinder)\nQTextBoundaryFinder(QTextBoundaryFinder.BoundaryType, str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def boundaryReasons(cls, self):
        'boundaryReasons(self) -> QTextBoundaryFinder.BoundaryReasons'
        pass
    
    @classmethod
    def isAtBoundary(cls, self):
        'isAtBoundary(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def position(cls, self):
        'position(self) -> int'
        return 1
    
    @classmethod
    def setPosition(cls, self, int):
        'setPosition(self, int)'
        pass
    
    @classmethod
    def string(cls, self):
        'string(self) -> str'
        return ''
    
    @classmethod
    def toEnd(cls, self):
        'toEnd(self)'
        pass
    
    @classmethod
    def toNextBoundary(cls, self):
        'toNextBoundary(self) -> int'
        return 1
    
    @classmethod
    def toPreviousBoundary(cls, self):
        'toPreviousBoundary(self) -> int'
        return 1
    
    @classmethod
    def toStart(cls, self):
        'toStart(self)'
        pass
    
    @classmethod
    def type(cls, self):
        'type(self) -> QTextBoundaryFinder.BoundaryType'
        pass
    

class QTextCodec(_mod_sip.wrapper):
    ConversionFlag = ConversionFlag
    ConversionFlags = ConversionFlags
    ConvertInvalidToNull = ConversionFlag()
    ConverterState = ConverterState
    DefaultConversion = ConversionFlag()
    IgnoreHeader = ConversionFlag()
    __class__ = QTextCodec
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def aliases(cls, self):
        'aliases(self) -> List[QByteArray]'
        pass
    
    @classmethod
    def availableCodecs(cls):
        'availableCodecs() -> List[QByteArray]'
        pass
    
    @classmethod
    def availableMibs(cls):
        'availableMibs() -> List[int]'
        pass
    
    @classmethod
    def canEncode(cls, self, str):
        'canEncode(self, str) -> bool'
        return True
    
    @classmethod
    def codecForHtml(cls, UnionQByteArray=None, bytes=None, bytearray=None, QTextCodec=None):
        'codecForHtml(Union[QByteArray, bytes, bytearray]) -> QTextCodec\ncodecForHtml(Union[QByteArray, bytes, bytearray], QTextCodec) -> QTextCodec'
        pass
    
    @classmethod
    def codecForLocale(cls):
        'codecForLocale() -> QTextCodec'
        pass
    
    @classmethod
    def codecForMib(cls, int):
        'codecForMib(int) -> QTextCodec'
        pass
    
    @classmethod
    def codecForName(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'codecForName(Union[QByteArray, bytes, bytearray]) -> QTextCodec\ncodecForName(str) -> QTextCodec'
        pass
    
    @classmethod
    def codecForUtfText(cls, UnionQByteArray=None, bytes=None, bytearray=None, QTextCodec=None):
        'codecForUtfText(Union[QByteArray, bytes, bytearray]) -> QTextCodec\ncodecForUtfText(Union[QByteArray, bytes, bytearray], QTextCodec) -> QTextCodec'
        pass
    
    @classmethod
    def fromUnicode(cls, self, str):
        'fromUnicode(self, str) -> QByteArray'
        pass
    
    @classmethod
    def makeDecoder(cls, self, flags: Union[QTextCodec.ConversionFlags,QTextCodec.ConversionFlag]=QTextCodec.DefaultConversion):
        'makeDecoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextDecoder'
        pass
    
    @classmethod
    def makeEncoder(cls, self, flags: Union[QTextCodec.ConversionFlags,QTextCodec.ConversionFlag]=QTextCodec.DefaultConversion):
        'makeEncoder(self, flags: Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag] = QTextCodec.DefaultConversion) -> QTextEncoder'
        pass
    
    @classmethod
    def mibEnum(cls, self):
        'mibEnum(self) -> int'
        return 1
    
    @classmethod
    def name(cls, self):
        'name(self) -> QByteArray'
        pass
    
    @classmethod
    def setCodecForLocale(cls, QTextCodec):
        'setCodecForLocale(QTextCodec)'
        pass
    
    @classmethod
    def toUnicode(cls, self, bytes, state: QTextCodec.ConverterState=None):
        'toUnicode(self, Union[QByteArray, bytes, bytearray]) -> str\ntoUnicode(self, str) -> str\ntoUnicode(self, bytes, state: QTextCodec.ConverterState = None) -> str'
        return ''
    

class QTextDecoder(_mod_sip.wrapper):
    'QTextDecoder(QTextCodec)\nQTextDecoder(QTextCodec, Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag])'
    __class__ = QTextDecoder
    __dict__ = {}
    def __init__(self, QTextCodec, UnionQTextCodecConversionFlags=None, QTextCodecConversionFlag=None):
        'QTextDecoder(QTextCodec)\nQTextDecoder(QTextCodec, Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def toUnicode(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'toUnicode(self, bytes) -> str\ntoUnicode(self, Union[QByteArray, bytes, bytearray]) -> str'
        return ''
    

class QTextEncoder(_mod_sip.wrapper):
    'QTextEncoder(QTextCodec)\nQTextEncoder(QTextCodec, Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag])'
    __class__ = QTextEncoder
    __dict__ = {}
    def __init__(self, QTextCodec, UnionQTextCodecConversionFlags=None, QTextCodecConversionFlag=None):
        'QTextEncoder(QTextCodec)\nQTextEncoder(QTextCodec, Union[QTextCodec.ConversionFlags, QTextCodec.ConversionFlag])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def fromUnicode(cls, self, str):
        'fromUnicode(self, str) -> QByteArray'
        pass
    

class QTextStream(_mod_sip.simplewrapper):
    'QTextStream()\nQTextStream(QIODevice)\nQTextStream(QByteArray, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)'
    AlignAccountingStyle = FieldAlignment()
    AlignCenter = FieldAlignment()
    AlignLeft = FieldAlignment()
    AlignRight = FieldAlignment()
    FieldAlignment = FieldAlignment
    FixedNotation = RealNumberNotation()
    ForcePoint = NumberFlag()
    ForceSign = NumberFlag()
    NumberFlag = NumberFlag
    NumberFlags = NumberFlags
    Ok = Status()
    ReadCorruptData = Status()
    ReadPastEnd = Status()
    RealNumberNotation = RealNumberNotation
    ScientificNotation = RealNumberNotation()
    ShowBase = NumberFlag()
    SmartNotation = RealNumberNotation()
    Status = Status
    UppercaseBase = NumberFlag()
    UppercaseDigits = NumberFlag()
    WriteFailed = Status()
    __class__ = QTextStream
    __dict__ = {}
    def __init__(self, QByteArray, mode: Union[QIODevice.OpenMode,QIODevice.OpenModeFlag]=QIODevice.ReadWrite):
        'QTextStream()\nQTextStream(QIODevice)\nQTextStream(QByteArray, mode: Union[QIODevice.OpenMode, QIODevice.OpenModeFlag] = QIODevice.ReadWrite)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __lshift__(self, value):
        'Return self<<value.'
        return QTextStream()
    
    __module__ = 'PyQt5.QtCore'
    def __rlshift__(self, value):
        'Return value<<self.'
        return QTextStream()
    
    def __rrshift__(self, value):
        'Return value>>self.'
        return QTextStream()
    
    def __rshift__(self, value):
        'Return self>>value.'
        return QTextStream()
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def autoDetectUnicode(cls, self):
        'autoDetectUnicode(self) -> bool'
        return True
    
    @classmethod
    def codec(cls, self):
        'codec(self) -> QTextCodec'
        pass
    
    @classmethod
    def device(cls, self):
        'device(self) -> QIODevice'
        pass
    
    @classmethod
    def fieldAlignment(cls, self):
        'fieldAlignment(self) -> QTextStream.FieldAlignment'
        pass
    
    @classmethod
    def fieldWidth(cls, self):
        'fieldWidth(self) -> int'
        return 1
    
    @classmethod
    def flush(cls, self):
        'flush(self)'
        pass
    
    @classmethod
    def generateByteOrderMark(cls, self):
        'generateByteOrderMark(self) -> bool'
        return True
    
    @classmethod
    def integerBase(cls, self):
        'integerBase(self) -> int'
        return 1
    
    @classmethod
    def locale(cls, self):
        'locale(self) -> QLocale'
        pass
    
    @classmethod
    def numberFlags(cls, self):
        'numberFlags(self) -> QTextStream.NumberFlags'
        pass
    
    @classmethod
    def padChar(cls, self):
        'padChar(self) -> str'
        return ''
    
    @classmethod
    def pos(cls, self):
        'pos(self) -> int'
        return 1
    
    @classmethod
    def read(cls, self, int):
        'read(self, int) -> str'
        return ''
    
    @classmethod
    def readAll(cls, self):
        'readAll(self) -> str'
        return ''
    
    @classmethod
    def readLine(cls, self, maxLength: int=0):
        'readLine(self, maxLength: int = 0) -> str'
        return ''
    
    @classmethod
    def realNumberNotation(cls, self):
        'realNumberNotation(self) -> QTextStream.RealNumberNotation'
        pass
    
    @classmethod
    def realNumberPrecision(cls, self):
        'realNumberPrecision(self) -> int'
        return 1
    
    @classmethod
    def reset(cls, self):
        'reset(self)'
        pass
    
    @classmethod
    def resetStatus(cls, self):
        'resetStatus(self)'
        pass
    
    @classmethod
    def seek(cls, self, int):
        'seek(self, int) -> bool'
        return True
    
    @classmethod
    def setAutoDetectUnicode(cls, self, bool):
        'setAutoDetectUnicode(self, bool)'
        pass
    
    @classmethod
    def setCodec(cls, self, QTextCodec):
        'setCodec(self, QTextCodec)\nsetCodec(self, str)'
        pass
    
    @classmethod
    def setDevice(cls, self, QIODevice):
        'setDevice(self, QIODevice)'
        pass
    
    @classmethod
    def setFieldAlignment(cls, self, QTextStreamFieldAlignment):
        'setFieldAlignment(self, QTextStream.FieldAlignment)'
        pass
    
    @classmethod
    def setFieldWidth(cls, self, int):
        'setFieldWidth(self, int)'
        pass
    
    @classmethod
    def setGenerateByteOrderMark(cls, self, bool):
        'setGenerateByteOrderMark(self, bool)'
        pass
    
    @classmethod
    def setIntegerBase(cls, self, int):
        'setIntegerBase(self, int)'
        pass
    
    @classmethod
    def setLocale(cls, self, QLocale):
        'setLocale(self, QLocale)'
        pass
    
    @classmethod
    def setNumberFlags(cls, self, UnionQTextStreamNumberFlags=None, QTextStreamNumberFlag=None):
        'setNumberFlags(self, Union[QTextStream.NumberFlags, QTextStream.NumberFlag])'
        pass
    
    @classmethod
    def setPadChar(cls, self, str):
        'setPadChar(self, str)'
        pass
    
    @classmethod
    def setRealNumberNotation(cls, self, QTextStreamRealNumberNotation):
        'setRealNumberNotation(self, QTextStream.RealNumberNotation)'
        pass
    
    @classmethod
    def setRealNumberPrecision(cls, self, int):
        'setRealNumberPrecision(self, int)'
        pass
    
    @classmethod
    def setStatus(cls, self, QTextStreamStatus):
        'setStatus(self, QTextStream.Status)'
        pass
    
    @classmethod
    def skipWhiteSpace(cls, self):
        'skipWhiteSpace(self)'
        pass
    
    @classmethod
    def status(cls, self):
        'status(self) -> QTextStream.Status'
        pass
    

class QTextStreamManipulator(_mod_sip.simplewrapper):
    __class__ = QTextStreamManipulator
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    

class QThread(QObject):
    'QThread(parent: QObject = None)'
    HighPriority = Priority()
    HighestPriority = Priority()
    IdlePriority = Priority()
    InheritPriority = Priority()
    LowPriority = Priority()
    LowestPriority = Priority()
    NormalPriority = Priority()
    Priority = Priority
    TimeCriticalPriority = Priority()
    __class__ = QThread
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QThread(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentThread(cls):
        'currentThread() -> QThread'
        pass
    
    @classmethod
    def currentThreadId(cls):
        'currentThreadId() -> sip.voidptr'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventDispatcher(cls, self):
        'eventDispatcher(self) -> QAbstractEventDispatcher'
        pass
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def exec(cls, self):
        'exec(self) -> int'
        return 1
    
    @classmethod
    def exec_(cls, self):
        'exec_(self) -> int'
        return 1
    
    @classmethod
    def exit(cls, self, returnCode: int=0):
        'exit(self, returnCode: int = 0)'
        pass
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    def finished(self):
        'finished(self) [signal]'
        pass
    
    @classmethod
    def idealThreadCount(cls):
        'idealThreadCount() -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isFinished(cls, self):
        'isFinished(self) -> bool'
        return True
    
    @classmethod
    def isInterruptionRequested(cls, self):
        'isInterruptionRequested(self) -> bool'
        return True
    
    @classmethod
    def isRunning(cls, self):
        'isRunning(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopLevel(cls, self):
        'loopLevel(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def msleep(cls, int):
        'msleep(int)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def priority(cls, self):
        'priority(self) -> QThread.Priority'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def quit(cls, self):
        'quit(self)'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def requestInterruption(cls, self):
        'requestInterruption(self)'
        pass
    
    @classmethod
    def run(cls, self):
        'run(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setEventDispatcher(cls, self, QAbstractEventDispatcher):
        'setEventDispatcher(self, QAbstractEventDispatcher)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPriority(cls, self, QThreadPriority):
        'setPriority(self, QThread.Priority)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setStackSize(cls, self, int):
        'setStackSize(self, int)'
        pass
    
    @classmethod
    def setTerminationEnabled(cls, enabled: bool=True):
        'setTerminationEnabled(enabled: bool = True)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def sleep(cls, int):
        'sleep(int)'
        pass
    
    @classmethod
    def stackSize(cls, self):
        'stackSize(self) -> int'
        return 1
    
    @classmethod
    def start(cls, self, priority: QThread.Priority=QThread.InheritPriority):
        'start(self, priority: QThread.Priority = QThread.InheritPriority)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    def started(self):
        'started(self) [signal]'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def terminate(cls, self):
        'terminate(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def usleep(cls, int):
        'usleep(int)'
        pass
    
    @classmethod
    def wait(cls, self, msecs: int=ULONG_MAX):
        'wait(self, msecs: int = ULONG_MAX) -> bool'
        return True
    
    @classmethod
    def yieldCurrentThread(cls):
        'yieldCurrentThread()'
        pass
    

class QThreadPool(QObject):
    'QThreadPool(parent: QObject = None)'
    __class__ = QThreadPool
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QThreadPool(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def activeThreadCount(cls, self):
        'activeThreadCount(self) -> int'
        return 1
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def cancel(cls, self, QRunnable):
        'cancel(self, QRunnable)'
        pass
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def expiryTimeout(cls, self):
        'expiryTimeout(self) -> int'
        return 1
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def globalInstance(cls):
        'globalInstance() -> QThreadPool'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def maxThreadCount(cls, self):
        'maxThreadCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def releaseThread(cls, self):
        'releaseThread(self)'
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def reserveThread(cls, self):
        'reserveThread(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setExpiryTimeout(cls, self, int):
        'setExpiryTimeout(self, int)'
        pass
    
    @classmethod
    def setMaxThreadCount(cls, self, int):
        'setMaxThreadCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, QRunnable, priority: int=0):
        'start(self, QRunnable, priority: int = 0)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def tryStart(cls, self, QRunnable):
        'tryStart(self, QRunnable) -> bool'
        return True
    
    @classmethod
    def tryTake(cls, self, QRunnable):
        'tryTake(self, QRunnable) -> bool'
        return True
    
    @classmethod
    def waitForDone(cls, self, msecs: int=-1):
        'waitForDone(self, msecs: int = -1) -> bool'
        return True
    

class QTime(_mod_sip.simplewrapper):
    'QTime()\nQTime(int, int, second: int = 0, msec: int = 0)\nQTime(QTime)'
    def __bool__(self):
        'self != 0'
        return False
    
    __class__ = QTime
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, int, int_, second: int=0, msec: int=0):
        'QTime()\nQTime(int, int, second: int = 0, msec: int = 0)\nQTime(QTime)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __reduce__(self):
        return ''; return ()
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addMSecs(cls, self, int):
        'addMSecs(self, int) -> QTime'
        pass
    
    @classmethod
    def addSecs(cls, self, int):
        'addSecs(self, int) -> QTime'
        pass
    
    @classmethod
    def currentTime(cls):
        'currentTime() -> QTime'
        pass
    
    @classmethod
    def elapsed(cls, self):
        'elapsed(self) -> int'
        return 1
    
    @classmethod
    def fromMSecsSinceStartOfDay(cls, int):
        'fromMSecsSinceStartOfDay(int) -> QTime'
        pass
    
    @classmethod
    def fromString(cls, str, format: Qt.DateFormat=Qt.TextDate):
        'fromString(str, format: Qt.DateFormat = Qt.TextDate) -> QTime\nfromString(str, str) -> QTime'
        pass
    
    @classmethod
    def hour(cls, self):
        'hour(self) -> int'
        return 1
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, int, int_, int_1, msec: int=0):
        'isValid(self) -> bool\nisValid(int, int, int, msec: int = 0) -> bool'
        return True
    
    @classmethod
    def minute(cls, self):
        'minute(self) -> int'
        return 1
    
    @classmethod
    def msec(cls, self):
        'msec(self) -> int'
        return 1
    
    @classmethod
    def msecsSinceStartOfDay(cls, self):
        'msecsSinceStartOfDay(self) -> int'
        return 1
    
    @classmethod
    def msecsTo(cls, self, UnionQTime=None, datetimetime=None):
        'msecsTo(self, Union[QTime, datetime.time]) -> int'
        return 1
    
    @classmethod
    def restart(cls, self):
        'restart(self) -> int'
        return 1
    
    @classmethod
    def second(cls, self):
        'second(self) -> int'
        return 1
    
    @classmethod
    def secsTo(cls, self, UnionQTime=None, datetimetime=None):
        'secsTo(self, Union[QTime, datetime.time]) -> int'
        return 1
    
    @classmethod
    def setHMS(cls, self, int, int_, int_1, msec: int=0):
        'setHMS(self, int, int, int, msec: int = 0) -> bool'
        return True
    
    @classmethod
    def start(cls, self):
        'start(self)'
        pass
    
    @classmethod
    def toPyTime(cls, self):
        'toPyTime(self) -> datetime.time'
        pass
    
    @classmethod
    def toString(cls, self, format: Qt.DateFormat=Qt.TextDate):
        'toString(self, format: Qt.DateFormat = Qt.TextDate) -> str\ntoString(self, str) -> str'
        return ''
    

class QTimeLine(QObject):
    'QTimeLine(duration: int = 1000, parent: QObject = None)'
    Backward = Direction()
    CosineCurve = CurveShape()
    CurveShape = CurveShape
    Direction = Direction
    EaseInCurve = CurveShape()
    EaseInOutCurve = CurveShape()
    EaseOutCurve = CurveShape()
    Forward = Direction()
    LinearCurve = CurveShape()
    NotRunning = State()
    Paused = State()
    Running = State()
    SineCurve = CurveShape()
    State = State
    __class__ = QTimeLine
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, duration: int=1000, parent: QObject=None):
        'QTimeLine(duration: int = 1000, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentFrame(cls, self):
        'currentFrame(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def currentValue(cls, self):
        'currentValue(self) -> float'
        return 1.0
    
    @classmethod
    def curveShape(cls, self):
        'curveShape(self) -> QTimeLine.CurveShape'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QTimeLine.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def easingCurve(cls, self):
        'easingCurve(self) -> QEasingCurve'
        pass
    
    @classmethod
    def endFrame(cls, self):
        'endFrame(self) -> int'
        return 1
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    def finished(self):
        'finished(self) [signal]'
        pass
    
    def frameChanged(self, int):
        'frameChanged(self, int) [signal]'
        pass
    
    @classmethod
    def frameForTime(cls, self, int):
        'frameForTime(self, int) -> int'
        return 1
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setCurveShape(cls, self, QTimeLineCurveShape):
        'setCurveShape(self, QTimeLine.CurveShape)'
        pass
    
    @classmethod
    def setDirection(cls, self, QTimeLineDirection):
        'setDirection(self, QTimeLine.Direction)'
        pass
    
    @classmethod
    def setDuration(cls, self, int):
        'setDuration(self, int)'
        pass
    
    @classmethod
    def setEasingCurve(cls, self, UnionQEasingCurve=None, QEasingCurveType=None):
        'setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type])'
        pass
    
    @classmethod
    def setEndFrame(cls, self, int):
        'setEndFrame(self, int)'
        pass
    
    @classmethod
    def setFrameRange(cls, self, int, int_):
        'setFrameRange(self, int, int)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setStartFrame(cls, self, int):
        'setStartFrame(self, int)'
        pass
    
    @classmethod
    def setUpdateInterval(cls, self, int):
        'setUpdateInterval(self, int)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self):
        'start(self)'
        pass
    
    @classmethod
    def startFrame(cls, self):
        'startFrame(self) -> int'
        return 1
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def state(cls, self):
        'state(self) -> QTimeLine.State'
        pass
    
    def stateChanged(self, QTimeLineState):
        'stateChanged(self, QTimeLine.State) [signal]'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def toggleDirection(cls, self):
        'toggleDirection(self)'
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateInterval(cls, self):
        'updateInterval(self) -> int'
        return 1
    
    def valueChanged(self, float):
        'valueChanged(self, float) [signal]'
        pass
    
    @classmethod
    def valueForTime(cls, self, int):
        'valueForTime(self, int) -> float'
        return 1.0
    

class QTimeZone(_mod_sip.simplewrapper):
    "QTimeZone()\nQTimeZone(Union[QByteArray, bytes, bytearray])\nQTimeZone(int)\nQTimeZone(Union[QByteArray, bytes, bytearray], int, str, str, country: QLocale.Country = QLocale.AnyCountry, comment: str = '')\nQTimeZone(QTimeZone)"
    DaylightTime = TimeType()
    DefaultName = NameType()
    GenericTime = TimeType()
    LongName = NameType()
    NameType = NameType
    OffsetData = OffsetData
    OffsetName = NameType()
    ShortName = NameType()
    StandardTime = TimeType()
    TimeType = TimeType
    __class__ = QTimeZone
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None, int=None, str=None, str_=None, country: QLocale.Country=QLocale.AnyCountry, comment: str=''):
        "QTimeZone()\nQTimeZone(Union[QByteArray, bytes, bytearray])\nQTimeZone(int)\nQTimeZone(Union[QByteArray, bytes, bytearray], int, str, str, country: QLocale.Country = QLocale.AnyCountry, comment: str = '')\nQTimeZone(QTimeZone)"
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def abbreviation(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'abbreviation(self, Union[QDateTime, datetime.datetime]) -> str'
        return ''
    
    @classmethod
    def availableTimeZoneIds(cls, QLocaleCountry):
        'availableTimeZoneIds() -> List[QByteArray]\navailableTimeZoneIds(QLocale.Country) -> List[QByteArray]\navailableTimeZoneIds(int) -> List[QByteArray]'
        pass
    
    @classmethod
    def comment(cls, self):
        'comment(self) -> str'
        return ''
    
    @classmethod
    def country(cls, self):
        'country(self) -> QLocale.Country'
        pass
    
    @classmethod
    def daylightTimeOffset(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'daylightTimeOffset(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def displayName(cls, self, UnionQDateTime=None, datetimedatetime=None, nameType: QTimeZone.NameType=QTimeZone.DefaultName, locale: QLocale=QLocale()):
        'displayName(self, Union[QDateTime, datetime.datetime], nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str\ndisplayName(self, QTimeZone.TimeType, nameType: QTimeZone.NameType = QTimeZone.DefaultName, locale: QLocale = QLocale()) -> str'
        return ''
    
    @classmethod
    def hasDaylightTime(cls, self):
        'hasDaylightTime(self) -> bool'
        return True
    
    @classmethod
    def hasTransitions(cls, self):
        'hasTransitions(self) -> bool'
        return True
    
    @classmethod
    def ianaIdToWindowsId(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'ianaIdToWindowsId(Union[QByteArray, bytes, bytearray]) -> QByteArray'
        pass
    
    @classmethod
    def id(cls, self):
        'id(self) -> QByteArray'
        pass
    
    @classmethod
    def isDaylightTime(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'isDaylightTime(self, Union[QDateTime, datetime.datetime]) -> bool'
        return True
    
    @classmethod
    def isTimeZoneIdAvailable(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'isTimeZoneIdAvailable(Union[QByteArray, bytes, bytearray]) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def nextTransition(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'nextTransition(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData'
        pass
    
    @classmethod
    def offsetData(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'offsetData(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData'
        pass
    
    @classmethod
    def offsetFromUtc(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'offsetFromUtc(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def previousTransition(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'previousTransition(self, Union[QDateTime, datetime.datetime]) -> QTimeZone.OffsetData'
        pass
    
    @classmethod
    def standardTimeOffset(cls, self, UnionQDateTime=None, datetimedatetime=None):
        'standardTimeOffset(self, Union[QDateTime, datetime.datetime]) -> int'
        return 1
    
    @classmethod
    def swap(cls, self, QTimeZone):
        'swap(self, QTimeZone)'
        pass
    
    @classmethod
    def systemTimeZone(cls):
        'systemTimeZone() -> QTimeZone'
        pass
    
    @classmethod
    def systemTimeZoneId(cls):
        'systemTimeZoneId() -> QByteArray'
        pass
    
    @classmethod
    def transitions(cls, self, UnionQDateTime=None, datetimedatetime=None, UnionQDateTime_=None, datetimedatetime_=None):
        'transitions(self, Union[QDateTime, datetime.datetime], Union[QDateTime, datetime.datetime]) -> object'
        pass
    
    @classmethod
    def utc(cls):
        'utc() -> QTimeZone'
        pass
    
    @classmethod
    def windowsIdToDefaultIanaId(cls, UnionQByteArray=None, bytes=None, bytearray=None, QLocaleCountry=None):
        'windowsIdToDefaultIanaId(Union[QByteArray, bytes, bytearray]) -> QByteArray\nwindowsIdToDefaultIanaId(Union[QByteArray, bytes, bytearray], QLocale.Country) -> QByteArray'
        pass
    
    @classmethod
    def windowsIdToIanaIds(cls, UnionQByteArray=None, bytes=None, bytearray=None, QLocaleCountry=None):
        'windowsIdToIanaIds(Union[QByteArray, bytes, bytearray]) -> List[QByteArray]\nwindowsIdToIanaIds(Union[QByteArray, bytes, bytearray], QLocale.Country) -> List[QByteArray]'
        pass
    

class QTimer(QObject):
    'QTimer(parent: QObject = None)'
    __class__ = QTimer
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QTimer(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def interval(cls, self):
        'interval(self) -> int'
        return 1
    
    @classmethod
    def isActive(cls, self):
        'isActive(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isSingleShot(cls, self):
        'isSingleShot(self) -> bool'
        return True
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def remainingTime(cls, self):
        'remainingTime(self) -> int'
        return 1
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setInterval(cls, self, int):
        'setInterval(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setSingleShot(cls, self, bool):
        'setSingleShot(self, bool)'
        pass
    
    @classmethod
    def setTimerType(cls, self, QtTimerType):
        'setTimerType(self, Qt.TimerType)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def singleShot(cls, int, QtTimerType, PYQT_SLOT):
        'singleShot(int, PYQT_SLOT)\nsingleShot(int, Qt.TimerType, PYQT_SLOT)'
        pass
    
    @classmethod
    def start(cls, self, int):
        'start(self, int)\nstart(self)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    def timeout(self):
        'timeout(self) [signal]'
        pass
    
    @classmethod
    def timerEvent(cls, self, QTimerEvent):
        'timerEvent(self, QTimerEvent)'
        pass
    
    @classmethod
    def timerId(cls, self):
        'timerId(self) -> int'
        return 1
    
    @classmethod
    def timerType(cls, self):
        'timerType(self) -> Qt.TimerType'
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QTimerEvent(QEvent):
    'QTimerEvent(int)\nQTimerEvent(QTimerEvent)'
    __class__ = QTimerEvent
    __dict__ = {}
    def __init__(self, QTimerEvent):
        'QTimerEvent(int)\nQTimerEvent(QTimerEvent)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def accept(cls, self):
        'accept(self)'
        pass
    
    @classmethod
    def ignore(cls, self):
        'ignore(self)'
        pass
    
    @classmethod
    def isAccepted(cls, self):
        'isAccepted(self) -> bool'
        return True
    
    @classmethod
    def registerEventType(cls, hint: int=-1):
        'registerEventType(hint: int = -1) -> int'
        return 1
    
    @classmethod
    def setAccepted(cls, self, bool):
        'setAccepted(self, bool)'
        pass
    
    @classmethod
    def spontaneous(cls, self):
        'spontaneous(self) -> bool'
        return True
    
    @classmethod
    def timerId(cls, self):
        'timerId(self) -> int'
        return 1
    
    @classmethod
    def type(cls, self):
        'type(self) -> QEvent.Type'
        pass
    

class QTranslator(QObject):
    'QTranslator(parent: QObject = None)'
    __class__ = QTranslator
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QTranslator(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def load(cls, self, str, directory: str='', searchDelimiters: str='', suffix: str=''):
        "load(self, str, directory: str = '', searchDelimiters: str = '', suffix: str = '') -> bool\nload(self, QLocale, str, prefix: str = '', directory: str = '', suffix: str = '') -> bool"
        return True
    
    @classmethod
    def loadFromData(cls, self, bytes, directory: str=''):
        "loadFromData(self, bytes, directory: str = '') -> bool"
        return True
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def translate(cls, self, str, str_, disambiguation: str=None, n: int=-1):
        'translate(self, str, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QUrl(_mod_sip.simplewrapper):
    'QUrl()\nQUrl(str, mode: QUrl.ParsingMode = QUrl.TolerantMode)\nQUrl(QUrl)'
    AssumeLocalFile = UserInputResolutionOption()
    ComponentFormattingOption = ComponentFormattingOption
    ComponentFormattingOptions = ComponentFormattingOptions
    DecodeReserved = ComponentFormattingOption()
    DecodedMode = ParsingMode()
    DefaultResolution = UserInputResolutionOption()
    EncodeDelimiters = ComponentFormattingOption()
    EncodeReserved = ComponentFormattingOption()
    EncodeSpaces = ComponentFormattingOption()
    EncodeUnicode = ComponentFormattingOption()
    FormattingOptions = FormattingOptions
    FullyDecoded = ComponentFormattingOption()
    FullyEncoded = ComponentFormattingOption()
    None_ = UrlFormattingOption()
    NormalizePathSegments = UrlFormattingOption()
    ParsingMode = ParsingMode
    PreferLocalFile = UrlFormattingOption()
    PrettyDecoded = ComponentFormattingOption()
    RemoveAuthority = UrlFormattingOption()
    RemoveFilename = UrlFormattingOption()
    RemoveFragment = UrlFormattingOption()
    RemovePassword = UrlFormattingOption()
    RemovePath = UrlFormattingOption()
    RemovePort = UrlFormattingOption()
    RemoveQuery = UrlFormattingOption()
    RemoveScheme = UrlFormattingOption()
    RemoveUserInfo = UrlFormattingOption()
    StrictMode = ParsingMode()
    StripTrailingSlash = UrlFormattingOption()
    TolerantMode = ParsingMode()
    UrlFormattingOption = UrlFormattingOption
    UserInputResolutionOption = UserInputResolutionOption
    UserInputResolutionOptions = UserInputResolutionOptions
    __class__ = QUrl
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'QUrl()\nQUrl(str, mode: QUrl.ParsingMode = QUrl.TolerantMode)\nQUrl(QUrl)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def adjusted(cls, self, QUrlFormattingOptions):
        'adjusted(self, QUrl.FormattingOptions) -> QUrl'
        pass
    
    @classmethod
    def authority(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'authority(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def detach(cls, self):
        'detach(self)'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def fileName(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.FullyDecoded):
        'fileName(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    
    @classmethod
    def fragment(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'fragment(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def fromAce(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'fromAce(Union[QByteArray, bytes, bytearray]) -> str'
        return ''
    
    @classmethod
    def fromEncoded(cls, UnionQByteArray=None, bytes=None, bytearray=None, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'fromEncoded(Union[QByteArray, bytes, bytearray], mode: QUrl.ParsingMode = QUrl.TolerantMode) -> QUrl'
        pass
    
    @classmethod
    def fromLocalFile(cls, str):
        'fromLocalFile(str) -> QUrl'
        pass
    
    @classmethod
    def fromPercentEncoding(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'fromPercentEncoding(Union[QByteArray, bytes, bytearray]) -> str'
        return ''
    
    @classmethod
    def fromStringList(cls, Iterablestr=None, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'fromStringList(Iterable[str], mode: QUrl.ParsingMode = QUrl.TolerantMode) -> List[QUrl]'
        pass
    
    @classmethod
    def fromUserInput(cls, str, str_, options: Union[QUrl.UserInputResolutionOptions,QUrl.UserInputResolutionOption]=QUrl.DefaultResolution):
        'fromUserInput(str) -> QUrl\nfromUserInput(str, str, options: Union[QUrl.UserInputResolutionOptions, QUrl.UserInputResolutionOption] = QUrl.DefaultResolution) -> QUrl'
        pass
    
    @classmethod
    def hasFragment(cls, self):
        'hasFragment(self) -> bool'
        return True
    
    @classmethod
    def hasQuery(cls, self):
        'hasQuery(self) -> bool'
        return True
    
    @classmethod
    def host(cls, self, UnionQUrlComponentFormattingOptions=None, QUrlComponentFormattingOption=QUrl.FullyDecoded):
        'host(self, Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    
    @classmethod
    def idnWhitelist(cls):
        'idnWhitelist() -> List[str]'
        pass
    
    @classmethod
    def isDetached(cls, self):
        'isDetached(self) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def isLocalFile(cls, self):
        'isLocalFile(self) -> bool'
        return True
    
    @classmethod
    def isParentOf(cls, self, QUrl):
        'isParentOf(self, QUrl) -> bool'
        return True
    
    @classmethod
    def isRelative(cls, self):
        'isRelative(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def matches(cls, self, QUrl, QUrlFormattingOptions):
        'matches(self, QUrl, QUrl.FormattingOptions) -> bool'
        return True
    
    @classmethod
    def password(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.FullyDecoded):
        'password(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    
    @classmethod
    def path(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.FullyDecoded):
        'path(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    
    @classmethod
    def port(cls, self, defaultPort: int=-1):
        'port(self, defaultPort: int = -1) -> int'
        return 1
    
    @classmethod
    def query(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'query(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def resolved(cls, self, QUrl):
        'resolved(self, QUrl) -> QUrl'
        pass
    
    @classmethod
    def scheme(cls, self):
        'scheme(self) -> str'
        return ''
    
    @classmethod
    def setAuthority(cls, self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'setAuthority(self, str, mode: QUrl.ParsingMode = QUrl.TolerantMode)'
        pass
    
    @classmethod
    def setFragment(cls, self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'setFragment(self, str, mode: QUrl.ParsingMode = QUrl.TolerantMode)'
        pass
    
    @classmethod
    def setHost(cls, self, str, mode: QUrl.ParsingMode=QUrl.DecodedMode):
        'setHost(self, str, mode: QUrl.ParsingMode = QUrl.DecodedMode)'
        pass
    
    @classmethod
    def setIdnWhitelist(cls, Iterablestr=None):
        'setIdnWhitelist(Iterable[str])'
        pass
    
    @classmethod
    def setPassword(cls, self, str, mode: QUrl.ParsingMode=QUrl.DecodedMode):
        'setPassword(self, str, mode: QUrl.ParsingMode = QUrl.DecodedMode)'
        pass
    
    @classmethod
    def setPath(cls, self, str, mode: QUrl.ParsingMode=QUrl.DecodedMode):
        'setPath(self, str, mode: QUrl.ParsingMode = QUrl.DecodedMode)'
        pass
    
    @classmethod
    def setPort(cls, self, int):
        'setPort(self, int)'
        pass
    
    @classmethod
    def setQuery(cls, self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'setQuery(self, str, mode: QUrl.ParsingMode = QUrl.TolerantMode)\nsetQuery(self, QUrlQuery)'
        pass
    
    @classmethod
    def setScheme(cls, self, str):
        'setScheme(self, str)'
        pass
    
    @classmethod
    def setUrl(cls, self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'setUrl(self, str, mode: QUrl.ParsingMode = QUrl.TolerantMode)'
        pass
    
    @classmethod
    def setUserInfo(cls, self, str, mode: QUrl.ParsingMode=QUrl.TolerantMode):
        'setUserInfo(self, str, mode: QUrl.ParsingMode = QUrl.TolerantMode)'
        pass
    
    @classmethod
    def setUserName(cls, self, str, mode: QUrl.ParsingMode=QUrl.DecodedMode):
        'setUserName(self, str, mode: QUrl.ParsingMode = QUrl.DecodedMode)'
        pass
    
    @classmethod
    def swap(cls, self, QUrl):
        'swap(self, QUrl)'
        pass
    
    @classmethod
    def toAce(cls, str):
        'toAce(str) -> QByteArray'
        pass
    
    @classmethod
    def toDisplayString(cls, self, options: QUrl.FormattingOptions=QUrl.PrettyDecoded):
        'toDisplayString(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def toEncoded(cls, self, options: QUrl.FormattingOptions=QUrl.FullyEncoded):
        'toEncoded(self, options: QUrl.FormattingOptions = QUrl.FullyEncoded) -> QByteArray'
        pass
    
    @classmethod
    def toLocalFile(cls, self):
        'toLocalFile(self) -> str'
        return ''
    
    @classmethod
    def toPercentEncoding(cls, str, exclude: Union[QByteArray,bytes,bytearray]=QByteArray(), include: Union[QByteArray,bytes,bytearray]=QByteArray()):
        'toPercentEncoding(str, exclude: Union[QByteArray, bytes, bytearray] = QByteArray(), include: Union[QByteArray, bytes, bytearray] = QByteArray()) -> QByteArray'
        pass
    
    @classmethod
    def toString(cls, self, options: QUrl.FormattingOptions=QUrl.PrettyDecoded):
        'toString(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def toStringList(cls, IterableQUrl=None, options: QUrl.FormattingOptions=QUrl.PrettyDecoded):
        'toStringList(Iterable[QUrl], options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> List[str]'
        pass
    
    @classmethod
    def topLevelDomain(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.FullyDecoded):
        'topLevelDomain(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    
    @classmethod
    def url(cls, self, options: QUrl.FormattingOptions=QUrl.PrettyDecoded):
        'url(self, options: QUrl.FormattingOptions = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def userInfo(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'userInfo(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def userName(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.FullyDecoded):
        'userName(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.FullyDecoded) -> str'
        return ''
    

class QUrlQuery(_mod_sip.simplewrapper):
    'QUrlQuery()\nQUrlQuery(QUrl)\nQUrlQuery(str)\nQUrlQuery(QUrlQuery)'
    __class__ = QUrlQuery
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QUrlQuery):
        'QUrlQuery()\nQUrlQuery(QUrl)\nQUrlQuery(str)\nQUrlQuery(QUrlQuery)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addQueryItem(cls, self, str, str_):
        'addQueryItem(self, str, str)'
        pass
    
    @classmethod
    def allQueryItemValues(cls, self, str, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'allQueryItemValues(self, str, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> List[str]'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def defaultQueryPairDelimiter(cls):
        'defaultQueryPairDelimiter() -> str'
        return ''
    
    @classmethod
    def defaultQueryValueDelimiter(cls):
        'defaultQueryValueDelimiter() -> str'
        return ''
    
    @classmethod
    def hasQueryItem(cls, self, str):
        'hasQueryItem(self, str) -> bool'
        return True
    
    @classmethod
    def isDetached(cls, self):
        'isDetached(self) -> bool'
        return True
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def query(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'query(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def queryItemValue(cls, self, str, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'queryItemValue(self, str, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    
    @classmethod
    def queryItems(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'queryItems(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> List[Tuple[str, str]]'
        pass
    
    @classmethod
    def queryPairDelimiter(cls, self):
        'queryPairDelimiter(self) -> str'
        return ''
    
    @classmethod
    def queryValueDelimiter(cls, self):
        'queryValueDelimiter(self) -> str'
        return ''
    
    @classmethod
    def removeAllQueryItems(cls, self, str):
        'removeAllQueryItems(self, str)'
        pass
    
    @classmethod
    def removeQueryItem(cls, self, str):
        'removeQueryItem(self, str)'
        pass
    
    @classmethod
    def setQuery(cls, self, str):
        'setQuery(self, str)'
        pass
    
    @classmethod
    def setQueryDelimiters(cls, self, str, str_):
        'setQueryDelimiters(self, str, str)'
        pass
    
    @classmethod
    def setQueryItems(cls, self, object):
        'setQueryItems(self, object)'
        pass
    
    @classmethod
    def swap(cls, self, QUrlQuery):
        'swap(self, QUrlQuery)'
        pass
    
    @classmethod
    def toString(cls, self, options: Union[QUrl.ComponentFormattingOptions,QUrl.ComponentFormattingOption]=QUrl.PrettyDecoded):
        'toString(self, options: Union[QUrl.ComponentFormattingOptions, QUrl.ComponentFormattingOption] = QUrl.PrettyDecoded) -> str'
        return ''
    

class QUuid(_mod_sip.simplewrapper):
    'QUuid()\nQUuid(int, int, int, int, int, int, int, int, int, int, int)\nQUuid(str)\nQUuid(Union[QByteArray, bytes, bytearray])\nQUuid(QUuid)'
    DCE = Variant()
    EmbeddedPOSIX = Version()
    Md5 = Version()
    Microsoft = Variant()
    NCS = Variant()
    Name = Version()
    Random = Version()
    Reserved = Variant()
    Sha1 = Version()
    Time = Version()
    VarUnknown = Variant()
    Variant = Variant
    VerUnknown = Version()
    Version = Version
    __class__ = QUuid
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, int, int_, int_1, int_2, int_3, int_4, int_5, int_6, int_7, int_8, int_9):
        'QUuid()\nQUuid(int, int, int, int, int, int, int, int, int, int, int)\nQUuid(str)\nQUuid(Union[QByteArray, bytes, bytearray])\nQUuid(QUuid)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def createUuid(cls):
        'createUuid() -> QUuid'
        pass
    
    @classmethod
    def createUuidV3(cls, QUuid, UnionQByteArray=None, bytes=None, bytearray=None):
        'createUuidV3(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid\ncreateUuidV3(QUuid, str) -> QUuid'
        pass
    
    @classmethod
    def createUuidV5(cls, QUuid, UnionQByteArray=None, bytes=None, bytearray=None):
        'createUuidV5(QUuid, Union[QByteArray, bytes, bytearray]) -> QUuid\ncreateUuidV5(QUuid, str) -> QUuid'
        pass
    
    @classmethod
    def fromRfc4122(cls, UnionQByteArray=None, bytes=None, bytearray=None):
        'fromRfc4122(Union[QByteArray, bytes, bytearray]) -> QUuid'
        pass
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def toByteArray(cls, self):
        'toByteArray(self) -> QByteArray'
        pass
    
    @classmethod
    def toRfc4122(cls, self):
        'toRfc4122(self) -> QByteArray'
        pass
    
    @classmethod
    def toString(cls, self):
        'toString(self) -> str'
        return ''
    
    @classmethod
    def variant(cls, self):
        'variant(self) -> QUuid.Variant'
        pass
    
    @classmethod
    def version(cls, self):
        'version(self) -> QUuid.Version'
        pass
    

class QVariant(_mod_sip.simplewrapper):
    'QVariant()\nQVariant(QVariant.Type)\nQVariant(object)\nQVariant(QVariant)'
    BitArray = Type()
    Bitmap = Type()
    Bool = Type()
    Brush = Type()
    ByteArray = Type()
    Char = Type()
    Color = Type()
    Cursor = Type()
    Date = Type()
    DateTime = Type()
    Double = Type()
    EasingCurve = Type()
    Font = Type()
    Hash = Type()
    Icon = Type()
    Image = Type()
    Int = Type()
    Invalid = Type()
    KeySequence = Type()
    Line = Type()
    LineF = Type()
    List = Type()
    Locale = Type()
    LongLong = Type()
    Map = Type()
    Matrix = Type()
    Matrix4x4 = Type()
    ModelIndex = Type()
    Palette = Type()
    Pen = Type()
    PersistentModelIndex = Type()
    Pixmap = Type()
    Point = Type()
    PointF = Type()
    Polygon = Type()
    PolygonF = Type()
    Quaternion = Type()
    Rect = Type()
    RectF = Type()
    RegExp = Type()
    Region = Type()
    RegularExpression = Type()
    Size = Type()
    SizeF = Type()
    SizePolicy = Type()
    String = Type()
    StringList = Type()
    TextFormat = Type()
    TextLength = Type()
    Time = Type()
    Transform = Type()
    Type = Type
    UInt = Type()
    ULongLong = Type()
    Url = Type()
    UserType = Type()
    Uuid = Type()
    Vector2D = Type()
    Vector3D = Type()
    Vector4D = Type()
    __class__ = QVariant
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QVariantType):
        'QVariant()\nQVariant(QVariant.Type)\nQVariant(object)\nQVariant(QVariant)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def canConvert(cls, self, int):
        'canConvert(self, int) -> bool'
        return True
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def convert(cls, self, int):
        'convert(self, int) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isValid(cls, self):
        'isValid(self) -> bool'
        return True
    
    @classmethod
    def load(cls, self, QDataStream):
        'load(self, QDataStream)'
        pass
    
    @classmethod
    def nameToType(cls, str):
        'nameToType(str) -> QVariant.Type'
        pass
    
    @classmethod
    def save(cls, self, QDataStream):
        'save(self, QDataStream)'
        pass
    
    @classmethod
    def swap(cls, self, QVariant):
        'swap(self, QVariant)'
        pass
    
    @classmethod
    def type(cls, self):
        'type(self) -> QVariant.Type'
        pass
    
    @classmethod
    def typeName(cls, self):
        'typeName(self) -> str'
        return ''
    
    @classmethod
    def typeToName(cls, int):
        'typeToName(int) -> str'
        return ''
    
    @classmethod
    def userType(cls, self):
        'userType(self) -> int'
        return 1
    
    @classmethod
    def value(cls, self):
        'value(self) -> object'
        pass
    

class QVariantAnimation(QAbstractAnimation):
    'QVariantAnimation(parent: QObject = None)'
    __class__ = QVariantAnimation
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, parent: QObject=None):
        'QVariantAnimation(parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def currentLoop(cls, self):
        'currentLoop(self) -> int'
        return 1
    
    @classmethod
    def currentLoopTime(cls, self):
        'currentLoopTime(self) -> int'
        return 1
    
    @classmethod
    def currentTime(cls, self):
        'currentTime(self) -> int'
        return 1
    
    @classmethod
    def currentValue(cls, self):
        'currentValue(self) -> Any'
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def direction(cls, self):
        'direction(self) -> QAbstractAnimation.Direction'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def duration(cls, self):
        'duration(self) -> int'
        return 1
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def easingCurve(cls, self):
        'easingCurve(self) -> QEasingCurve'
        pass
    
    @classmethod
    def endValue(cls, self):
        'endValue(self) -> Any'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def group(cls, self):
        'group(self) -> QAnimationGroup'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def interpolated(cls, self, Any, Any_, float):
        'interpolated(self, Any, Any, float) -> Any'
        pass
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def keyValueAt(cls, self, float):
        'keyValueAt(self, float) -> Any'
        pass
    
    @classmethod
    def keyValues(cls, self):
        'keyValues(self) -> object'
        pass
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def loopCount(cls, self):
        'loopCount(self) -> int'
        return 1
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def pause(cls, self):
        'pause(self)'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def resume(cls, self):
        'resume(self)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setCurrentTime(cls, self, int):
        'setCurrentTime(self, int)'
        pass
    
    @classmethod
    def setDirection(cls, self, QAbstractAnimationDirection):
        'setDirection(self, QAbstractAnimation.Direction)'
        pass
    
    @classmethod
    def setDuration(cls, self, int):
        'setDuration(self, int)'
        pass
    
    @classmethod
    def setEasingCurve(cls, self, UnionQEasingCurve=None, QEasingCurveType=None):
        'setEasingCurve(self, Union[QEasingCurve, QEasingCurve.Type])'
        pass
    
    @classmethod
    def setEndValue(cls, self, Any):
        'setEndValue(self, Any)'
        pass
    
    @classmethod
    def setKeyValueAt(cls, self, float, Any):
        'setKeyValueAt(self, float, Any)'
        pass
    
    @classmethod
    def setKeyValues(cls, self, object):
        'setKeyValues(self, object)'
        pass
    
    @classmethod
    def setLoopCount(cls, self, int):
        'setLoopCount(self, int)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setPaused(cls, self, bool):
        'setPaused(self, bool)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def setStartValue(cls, self, Any):
        'setStartValue(self, Any)'
        pass
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def start(cls, self, policy: QAbstractAnimation.DeletionPolicy=QAbstractAnimation.KeepWhenStopped):
        'start(self, policy: QAbstractAnimation.DeletionPolicy = QAbstractAnimation.KeepWhenStopped)'
        pass
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    @classmethod
    def startValue(cls, self):
        'startValue(self) -> Any'
        pass
    
    @classmethod
    def state(cls, self):
        'state(self) -> QAbstractAnimation.State'
        pass
    
    staticMetaObject = QMetaObject()
    @classmethod
    def stop(cls, self):
        'stop(self)'
        pass
    
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def totalDuration(cls, self):
        'totalDuration(self) -> int'
        return 1
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    
    @classmethod
    def updateCurrentTime(cls, self, int):
        'updateCurrentTime(self, int)'
        pass
    
    @classmethod
    def updateCurrentValue(cls, self, Any):
        'updateCurrentValue(self, Any)'
        pass
    
    @classmethod
    def updateDirection(cls):
        pass
    
    @classmethod
    def updateState(cls, self, QAbstractAnimationState, QAbstractAnimationState_):
        'updateState(self, QAbstractAnimation.State, QAbstractAnimation.State)'
        pass
    
    def valueChanged(self, Any):
        'valueChanged(self, Any) [signal]'
        pass
    

class QVersionNumber(_mod_sip.simplewrapper):
    'QVersionNumber()\nQVersionNumber(Iterable[int])\nQVersionNumber(int)\nQVersionNumber(int, int)\nQVersionNumber(int, int, int)\nQVersionNumber(QVersionNumber)'
    __class__ = QVersionNumber
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    def __hash__(self):
        'Return hash(self).'
        return 0
    
    def __init__(self, QVersionNumber):
        'QVersionNumber()\nQVersionNumber(Iterable[int])\nQVersionNumber(int)\nQVersionNumber(int, int)\nQVersionNumber(int, int, int)\nQVersionNumber(QVersionNumber)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def commonPrefix(cls, QVersionNumber, QVersionNumber_):
        'commonPrefix(QVersionNumber, QVersionNumber) -> QVersionNumber'
        pass
    
    @classmethod
    def compare(cls, QVersionNumber, QVersionNumber_):
        'compare(QVersionNumber, QVersionNumber) -> int'
        return 1
    
    @classmethod
    def fromString(cls, str):
        'fromString(str) -> Tuple[QVersionNumber, int]'
        pass
    
    @classmethod
    def isNormalized(cls, self):
        'isNormalized(self) -> bool'
        return True
    
    @classmethod
    def isNull(cls, self):
        'isNull(self) -> bool'
        return True
    
    @classmethod
    def isPrefixOf(cls, self, QVersionNumber):
        'isPrefixOf(self, QVersionNumber) -> bool'
        return True
    
    @classmethod
    def majorVersion(cls, self):
        'majorVersion(self) -> int'
        return 1
    
    @classmethod
    def microVersion(cls, self):
        'microVersion(self) -> int'
        return 1
    
    @classmethod
    def minorVersion(cls, self):
        'minorVersion(self) -> int'
        return 1
    
    @classmethod
    def normalized(cls, self):
        'normalized(self) -> QVersionNumber'
        pass
    
    @classmethod
    def segmentAt(cls, self, int):
        'segmentAt(self, int) -> int'
        return 1
    
    @classmethod
    def segmentCount(cls, self):
        'segmentCount(self) -> int'
        return 1
    
    @classmethod
    def segments(cls, self):
        'segments(self) -> List[int]'
        pass
    
    @classmethod
    def toString(cls, self):
        'toString(self) -> str'
        return ''
    

class QWaitCondition(_mod_sip.simplewrapper):
    'QWaitCondition()'
    __class__ = QWaitCondition
    __dict__ = {}
    def __init__(self):
        'QWaitCondition()'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def wait(cls, self, QReadWriteLock, msecs: int=ULONG_MAX):
        'wait(self, QMutex, msecs: int = ULONG_MAX) -> bool\nwait(self, QReadWriteLock, msecs: int = ULONG_MAX) -> bool'
        return True
    
    @classmethod
    def wakeAll(cls, self):
        'wakeAll(self)'
        pass
    
    @classmethod
    def wakeOne(cls, self):
        'wakeOne(self)'
        pass
    

class QWinEventNotifier(QObject):
    'QWinEventNotifier(parent: QObject = None)\nQWinEventNotifier(sip.voidptr, parent: QObject = None)'
    __class__ = QWinEventNotifier
    __dict__ = {}
    @classmethod
    def __getattr__(cls, self, str):
        '__getattr__(self, str) -> object'
        pass
    
    def __init__(self, sipvoidptr, parent: QObject=None):
        'QWinEventNotifier(parent: QObject = None)\nQWinEventNotifier(sip.voidptr, parent: QObject = None)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def activated(self, sipvoidptr):
        'activated(self, sip.voidptr) [signal]'
        pass
    
    @classmethod
    def blockSignals(cls, self, bool):
        'blockSignals(self, bool) -> bool'
        return True
    
    @classmethod
    def childEvent(cls):
        pass
    
    @classmethod
    def children(cls, self):
        'children(self) -> object'
        pass
    
    @classmethod
    def connectNotify(cls):
        pass
    
    @classmethod
    def customEvent(cls):
        pass
    
    @classmethod
    def deleteLater(cls, self):
        'deleteLater(self)'
        pass
    
    @classmethod
    def disconnect(cls, self):
        'disconnect(self)'
        pass
    
    @classmethod
    def disconnectNotify(cls):
        pass
    
    @classmethod
    def dumpObjectInfo(cls, self):
        'dumpObjectInfo(self)'
        pass
    
    @classmethod
    def dumpObjectTree(cls, self):
        'dumpObjectTree(self)'
        pass
    
    @classmethod
    def dynamicPropertyNames(cls, self):
        'dynamicPropertyNames(self) -> object'
        pass
    
    @classmethod
    def event(cls, self, QEvent):
        'event(self, QEvent) -> bool'
        return True
    
    @classmethod
    def eventFilter(cls, self, QObject, QEvent):
        'eventFilter(self, QObject, QEvent) -> bool'
        return True
    
    @classmethod
    def findChild(cls, self, Tuple, name: str='', options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChild(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject\nfindChild(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> QObject"
        pass
    
    @classmethod
    def findChildren(cls, self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions,Qt.FindChildOption]=Qt.FindChildrenRecursively):
        "findChildren(self, type, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, name: str = '', options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegExp, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, type, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]\nfindChildren(self, Tuple, QRegularExpression, options: Union[Qt.FindChildOptions, Qt.FindChildOption] = Qt.FindChildrenRecursively) -> List[QObject]"
        pass
    
    @classmethod
    def handle(cls, self):
        'handle(self) -> sip.voidptr'
        pass
    
    @classmethod
    def inherits(cls, self, str):
        'inherits(self, str) -> bool'
        return True
    
    @classmethod
    def installEventFilter(cls, self, QObject):
        'installEventFilter(self, QObject)'
        pass
    
    @classmethod
    def isEnabled(cls, self):
        'isEnabled(self) -> bool'
        return True
    
    @classmethod
    def isSignalConnected(cls):
        pass
    
    @classmethod
    def isWidgetType(cls, self):
        'isWidgetType(self) -> bool'
        return True
    
    @classmethod
    def isWindowType(cls, self):
        'isWindowType(self) -> bool'
        return True
    
    @classmethod
    def killTimer(cls, self, int):
        'killTimer(self, int)'
        pass
    
    @classmethod
    def metaObject(cls, self):
        'metaObject(self) -> QMetaObject'
        pass
    
    @classmethod
    def moveToThread(cls, self, QThread):
        'moveToThread(self, QThread)'
        pass
    
    @classmethod
    def objectName(cls, self):
        'objectName(self) -> str'
        return ''
    
    @classmethod
    def parent(cls, self):
        'parent(self) -> QObject'
        pass
    
    @classmethod
    def property(cls, self, str):
        'property(self, str) -> Any'
        pass
    
    @classmethod
    def pyqtConfigure(cls):
        'QObject.pyqtConfigure(...)\n\nEach keyword argument is either the name of a Qt property or a Qt signal.\nFor properties the property is set to the given value which should be of an\nappropriate type.\nFor signals the signal is connected to the given value which should be a\ncallable.'
        pass
    
    @classmethod
    def receivers(cls):
        pass
    
    @classmethod
    def removeEventFilter(cls, self, QObject):
        'removeEventFilter(self, QObject)'
        pass
    
    @classmethod
    def sender(cls):
        pass
    
    @classmethod
    def senderSignalIndex(cls):
        pass
    
    @classmethod
    def setEnabled(cls, self, bool):
        'setEnabled(self, bool)'
        pass
    
    @classmethod
    def setHandle(cls, self, sipvoidptr):
        'setHandle(self, sip.voidptr)'
        pass
    
    @classmethod
    def setObjectName(cls, self, str):
        'setObjectName(self, str)'
        pass
    
    @classmethod
    def setParent(cls, self, QObject):
        'setParent(self, QObject)'
        pass
    
    @classmethod
    def setProperty(cls, self, str, Any):
        'setProperty(self, str, Any) -> bool'
        return True
    
    @classmethod
    def signalsBlocked(cls, self):
        'signalsBlocked(self) -> bool'
        return True
    
    @classmethod
    def startTimer(cls, self, int, timerType: Qt.TimerType=Qt.CoarseTimer):
        'startTimer(self, int, timerType: Qt.TimerType = Qt.CoarseTimer) -> int'
        return 1
    
    staticMetaObject = QMetaObject()
    @classmethod
    def thread(cls, self):
        'thread(self) -> QThread'
        pass
    
    @classmethod
    def timerEvent(cls):
        pass
    
    @classmethod
    def tr(cls, self, str, disambiguation: str=None, n: int=-1):
        'tr(self, str, disambiguation: str = None, n: int = -1) -> str'
        return ''
    

class QWriteLocker(_mod_sip.simplewrapper):
    'QWriteLocker(QReadWriteLock)'
    __class__ = QWriteLocker
    __dict__ = {}
    @classmethod
    def __enter__(cls, self):
        '__enter__(self) -> object'
        return self
    
    @classmethod
    def __exit__(cls, self, object, object_, object_1):
        '__exit__(self, object, object, object)'
        pass
    
    def __init__(self, QReadWriteLock):
        'QWriteLocker(QReadWriteLock)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def readWriteLock(cls, self):
        'readWriteLock(self) -> QReadWriteLock'
        pass
    
    @classmethod
    def relock(cls, self):
        'relock(self)'
        pass
    
    @classmethod
    def unlock(cls, self):
        'unlock(self)'
        pass
    

class QXmlStreamAttribute(_mod_sip.simplewrapper):
    'QXmlStreamAttribute()\nQXmlStreamAttribute(str, str)\nQXmlStreamAttribute(str, str, str)\nQXmlStreamAttribute(QXmlStreamAttribute)'
    __class__ = QXmlStreamAttribute
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QXmlStreamAttribute):
        'QXmlStreamAttribute()\nQXmlStreamAttribute(str, str)\nQXmlStreamAttribute(str, str, str)\nQXmlStreamAttribute(QXmlStreamAttribute)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def isDefault(cls, self):
        'isDefault(self) -> bool'
        return True
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def namespaceUri(cls, self):
        'namespaceUri(self) -> str'
        return ''
    
    @classmethod
    def prefix(cls, self):
        'prefix(self) -> str'
        return ''
    
    @classmethod
    def qualifiedName(cls, self):
        'qualifiedName(self) -> str'
        return ''
    
    @classmethod
    def value(cls, self):
        'value(self) -> str'
        return ''
    

class QXmlStreamAttributes(_mod_sip.simplewrapper):
    'QXmlStreamAttributes()\nQXmlStreamAttributes(QXmlStreamAttributes)'
    __class__ = QXmlStreamAttributes
    def __contains__(self, key):
        'Return key in self.'
        return False
    
    def __delitem__(self, key):
        'Delete self[key].'
        return None
    
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __iadd__(self, value):
        'Implement self+=value.'
        return None
    
    def __init__(self, QXmlStreamAttributes):
        'QXmlStreamAttributes()\nQXmlStreamAttributes(QXmlStreamAttributes)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __len__(self):
        'Return len(self).'
        return 0
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    def __setitem__(self, key, value):
        'Set self[key] to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def append(cls, self, QXmlStreamAttribute):
        'append(self, str, str, str)\nappend(self, str, str)\nappend(self, QXmlStreamAttribute)'
        pass
    
    @classmethod
    def at(cls, self, int):
        'at(self, int) -> QXmlStreamAttribute'
        pass
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def contains(cls, self, QXmlStreamAttribute):
        'contains(self, QXmlStreamAttribute) -> bool'
        return True
    
    @classmethod
    def count(cls, self, QXmlStreamAttribute):
        'count(self, QXmlStreamAttribute) -> int\ncount(self) -> int'
        return 1
    
    @classmethod
    def data(cls, self):
        'data(self) -> sip.voidptr'
        pass
    
    @classmethod
    def fill(cls, self, QXmlStreamAttribute, size: int=-1):
        'fill(self, QXmlStreamAttribute, size: int = -1)'
        pass
    
    @classmethod
    def first(cls, self):
        'first(self) -> QXmlStreamAttribute'
        pass
    
    @classmethod
    def hasAttribute(cls, self, str, str_):
        'hasAttribute(self, str) -> bool\nhasAttribute(self, str, str) -> bool'
        return True
    
    @classmethod
    def indexOf(cls, self, QXmlStreamAttribute, from_: int=0):
        'indexOf(self, QXmlStreamAttribute, from_: int = 0) -> int'
        return 1
    
    @classmethod
    def insert(cls, self, int, QXmlStreamAttribute):
        'insert(self, int, QXmlStreamAttribute)'
        pass
    
    @classmethod
    def isEmpty(cls, self):
        'isEmpty(self) -> bool'
        return True
    
    @classmethod
    def last(cls, self):
        'last(self) -> QXmlStreamAttribute'
        pass
    
    @classmethod
    def lastIndexOf(cls, self, QXmlStreamAttribute, from_: int=-1):
        'lastIndexOf(self, QXmlStreamAttribute, from_: int = -1) -> int'
        return 1
    
    @classmethod
    def prepend(cls, self, QXmlStreamAttribute):
        'prepend(self, QXmlStreamAttribute)'
        pass
    
    @classmethod
    def remove(cls, self, int, int_):
        'remove(self, int)\nremove(self, int, int)'
        pass
    
    @classmethod
    def replace(cls, self, int, QXmlStreamAttribute):
        'replace(self, int, QXmlStreamAttribute)'
        pass
    
    @classmethod
    def size(cls, self):
        'size(self) -> int'
        return 1
    
    @classmethod
    def value(cls, self, str, str_):
        'value(self, str, str) -> str\nvalue(self, str) -> str'
        return ''
    

class QXmlStreamEntityDeclaration(_mod_sip.simplewrapper):
    'QXmlStreamEntityDeclaration()\nQXmlStreamEntityDeclaration(QXmlStreamEntityDeclaration)'
    __class__ = QXmlStreamEntityDeclaration
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QXmlStreamEntityDeclaration):
        'QXmlStreamEntityDeclaration()\nQXmlStreamEntityDeclaration(QXmlStreamEntityDeclaration)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def notationName(cls, self):
        'notationName(self) -> str'
        return ''
    
    @classmethod
    def publicId(cls, self):
        'publicId(self) -> str'
        return ''
    
    @classmethod
    def systemId(cls, self):
        'systemId(self) -> str'
        return ''
    
    @classmethod
    def value(cls, self):
        'value(self) -> str'
        return ''
    

class QXmlStreamEntityResolver(_mod_sip.simplewrapper):
    'QXmlStreamEntityResolver()\nQXmlStreamEntityResolver(QXmlStreamEntityResolver)'
    __class__ = QXmlStreamEntityResolver
    __dict__ = {}
    def __init__(self, QXmlStreamEntityResolver):
        'QXmlStreamEntityResolver()\nQXmlStreamEntityResolver(QXmlStreamEntityResolver)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def resolveUndeclaredEntity(cls, self, str):
        'resolveUndeclaredEntity(self, str) -> str'
        return ''
    

class QXmlStreamNamespaceDeclaration(_mod_sip.simplewrapper):
    'QXmlStreamNamespaceDeclaration()\nQXmlStreamNamespaceDeclaration(QXmlStreamNamespaceDeclaration)\nQXmlStreamNamespaceDeclaration(str, str)'
    __class__ = QXmlStreamNamespaceDeclaration
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QXmlStreamNamespaceDeclaration):
        'QXmlStreamNamespaceDeclaration()\nQXmlStreamNamespaceDeclaration(QXmlStreamNamespaceDeclaration)\nQXmlStreamNamespaceDeclaration(str, str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def namespaceUri(cls, self):
        'namespaceUri(self) -> str'
        return ''
    
    @classmethod
    def prefix(cls, self):
        'prefix(self) -> str'
        return ''
    

class QXmlStreamNotationDeclaration(_mod_sip.simplewrapper):
    'QXmlStreamNotationDeclaration()\nQXmlStreamNotationDeclaration(QXmlStreamNotationDeclaration)'
    __class__ = QXmlStreamNotationDeclaration
    __dict__ = {}
    def __eq__(self, value):
        'Return self==value.'
        return False
    
    def __ge__(self, value):
        'Return self>=value.'
        return False
    
    def __gt__(self, value):
        'Return self>value.'
        return False
    
    __hash__ = None
    def __init__(self, QXmlStreamNotationDeclaration):
        'QXmlStreamNotationDeclaration()\nQXmlStreamNotationDeclaration(QXmlStreamNotationDeclaration)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    def __le__(self, value):
        'Return self<=value.'
        return False
    
    def __lt__(self, value):
        'Return self<value.'
        return False
    
    __module__ = 'PyQt5.QtCore'
    def __ne__(self, value):
        'Return self!=value.'
        return False
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def publicId(cls, self):
        'publicId(self) -> str'
        return ''
    
    @classmethod
    def systemId(cls, self):
        'systemId(self) -> str'
        return ''
    

class QXmlStreamReader(_mod_sip.simplewrapper):
    'QXmlStreamReader()\nQXmlStreamReader(QIODevice)\nQXmlStreamReader(Union[QByteArray, bytes, bytearray])\nQXmlStreamReader(str)'
    Characters = TokenType()
    Comment = TokenType()
    CustomError = Error()
    DTD = TokenType()
    EndDocument = TokenType()
    EndElement = TokenType()
    EntityReference = TokenType()
    Error = Error
    ErrorOnUnexpectedElement = ReadElementTextBehaviour()
    IncludeChildElements = ReadElementTextBehaviour()
    Invalid = TokenType()
    NoError = Error()
    NoToken = TokenType()
    NotWellFormedError = Error()
    PrematureEndOfDocumentError = Error()
    ProcessingInstruction = TokenType()
    ReadElementTextBehaviour = ReadElementTextBehaviour
    SkipChildElements = ReadElementTextBehaviour()
    StartDocument = TokenType()
    StartElement = TokenType()
    TokenType = TokenType
    UnexpectedElementError = Error()
    __class__ = QXmlStreamReader
    __dict__ = {}
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None):
        'QXmlStreamReader()\nQXmlStreamReader(QIODevice)\nQXmlStreamReader(Union[QByteArray, bytes, bytearray])\nQXmlStreamReader(str)'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def addData(cls, self, UnionQByteArray=None, bytes=None, bytearray=None):
        'addData(self, Union[QByteArray, bytes, bytearray])\naddData(self, str)'
        pass
    
    @classmethod
    def addExtraNamespaceDeclaration(cls, self, QXmlStreamNamespaceDeclaration):
        'addExtraNamespaceDeclaration(self, QXmlStreamNamespaceDeclaration)'
        pass
    
    @classmethod
    def addExtraNamespaceDeclarations(cls, self, object):
        'addExtraNamespaceDeclarations(self, object)'
        pass
    
    @classmethod
    def atEnd(cls, self):
        'atEnd(self) -> bool'
        return True
    
    @classmethod
    def attributes(cls, self):
        'attributes(self) -> QXmlStreamAttributes'
        pass
    
    @classmethod
    def characterOffset(cls, self):
        'characterOffset(self) -> int'
        return 1
    
    @classmethod
    def clear(cls, self):
        'clear(self)'
        pass
    
    @classmethod
    def columnNumber(cls, self):
        'columnNumber(self) -> int'
        return 1
    
    @classmethod
    def device(cls, self):
        'device(self) -> QIODevice'
        pass
    
    @classmethod
    def documentEncoding(cls, self):
        'documentEncoding(self) -> str'
        return ''
    
    @classmethod
    def documentVersion(cls, self):
        'documentVersion(self) -> str'
        return ''
    
    @classmethod
    def dtdName(cls, self):
        'dtdName(self) -> str'
        return ''
    
    @classmethod
    def dtdPublicId(cls, self):
        'dtdPublicId(self) -> str'
        return ''
    
    @classmethod
    def dtdSystemId(cls, self):
        'dtdSystemId(self) -> str'
        return ''
    
    @classmethod
    def entityDeclarations(cls, self):
        'entityDeclarations(self) -> object'
        pass
    
    @classmethod
    def entityResolver(cls, self):
        'entityResolver(self) -> QXmlStreamEntityResolver'
        pass
    
    @classmethod
    def error(cls, self):
        'error(self) -> QXmlStreamReader.Error'
        pass
    
    @classmethod
    def errorString(cls, self):
        'errorString(self) -> str'
        return ''
    
    @classmethod
    def hasError(cls, self):
        'hasError(self) -> bool'
        return True
    
    @classmethod
    def isCDATA(cls, self):
        'isCDATA(self) -> bool'
        return True
    
    @classmethod
    def isCharacters(cls, self):
        'isCharacters(self) -> bool'
        return True
    
    @classmethod
    def isComment(cls, self):
        'isComment(self) -> bool'
        return True
    
    @classmethod
    def isDTD(cls, self):
        'isDTD(self) -> bool'
        return True
    
    @classmethod
    def isEndDocument(cls, self):
        'isEndDocument(self) -> bool'
        return True
    
    @classmethod
    def isEndElement(cls, self):
        'isEndElement(self) -> bool'
        return True
    
    @classmethod
    def isEntityReference(cls, self):
        'isEntityReference(self) -> bool'
        return True
    
    @classmethod
    def isProcessingInstruction(cls, self):
        'isProcessingInstruction(self) -> bool'
        return True
    
    @classmethod
    def isStandaloneDocument(cls, self):
        'isStandaloneDocument(self) -> bool'
        return True
    
    @classmethod
    def isStartDocument(cls, self):
        'isStartDocument(self) -> bool'
        return True
    
    @classmethod
    def isStartElement(cls, self):
        'isStartElement(self) -> bool'
        return True
    
    @classmethod
    def isWhitespace(cls, self):
        'isWhitespace(self) -> bool'
        return True
    
    @classmethod
    def lineNumber(cls, self):
        'lineNumber(self) -> int'
        return 1
    
    @classmethod
    def name(cls, self):
        'name(self) -> str'
        return ''
    
    @classmethod
    def namespaceDeclarations(cls, self):
        'namespaceDeclarations(self) -> object'
        pass
    
    @classmethod
    def namespaceProcessing(cls, self):
        'namespaceProcessing(self) -> bool'
        return True
    
    @classmethod
    def namespaceUri(cls, self):
        'namespaceUri(self) -> str'
        return ''
    
    @classmethod
    def notationDeclarations(cls, self):
        'notationDeclarations(self) -> object'
        pass
    
    @classmethod
    def prefix(cls, self):
        'prefix(self) -> str'
        return ''
    
    @classmethod
    def processingInstructionData(cls, self):
        'processingInstructionData(self) -> str'
        return ''
    
    @classmethod
    def processingInstructionTarget(cls, self):
        'processingInstructionTarget(self) -> str'
        return ''
    
    @classmethod
    def qualifiedName(cls, self):
        'qualifiedName(self) -> str'
        return ''
    
    @classmethod
    def raiseError(cls, self, message: str=''):
        "raiseError(self, message: str = '')"
        pass
    
    @classmethod
    def readElementText(cls, self, behaviour: QXmlStreamReader.ReadElementTextBehaviour=QXmlStreamReader.ErrorOnUnexpectedElement):
        'readElementText(self, behaviour: QXmlStreamReader.ReadElementTextBehaviour = QXmlStreamReader.ErrorOnUnexpectedElement) -> str'
        return ''
    
    @classmethod
    def readNext(cls, self):
        'readNext(self) -> QXmlStreamReader.TokenType'
        pass
    
    @classmethod
    def readNextStartElement(cls, self):
        'readNextStartElement(self) -> bool'
        return True
    
    @classmethod
    def setDevice(cls, self, QIODevice):
        'setDevice(self, QIODevice)'
        pass
    
    @classmethod
    def setEntityResolver(cls, self, QXmlStreamEntityResolver):
        'setEntityResolver(self, QXmlStreamEntityResolver)'
        pass
    
    @classmethod
    def setNamespaceProcessing(cls, self, bool):
        'setNamespaceProcessing(self, bool)'
        pass
    
    @classmethod
    def skipCurrentElement(cls, self):
        'skipCurrentElement(self)'
        pass
    
    @classmethod
    def text(cls, self):
        'text(self) -> str'
        return ''
    
    @classmethod
    def tokenString(cls, self):
        'tokenString(self) -> str'
        return ''
    
    @classmethod
    def tokenType(cls, self):
        'tokenType(self) -> QXmlStreamReader.TokenType'
        pass
    

class QXmlStreamWriter(_mod_sip.simplewrapper):
    'QXmlStreamWriter()\nQXmlStreamWriter(QIODevice)\nQXmlStreamWriter(Union[QByteArray, bytes, bytearray])'
    __class__ = QXmlStreamWriter
    __dict__ = {}
    def __init__(self, UnionQByteArray=None, bytes=None, bytearray=None):
        'QXmlStreamWriter()\nQXmlStreamWriter(QIODevice)\nQXmlStreamWriter(Union[QByteArray, bytes, bytearray])'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    @classmethod
    def autoFormatting(cls, self):
        'autoFormatting(self) -> bool'
        return True
    
    @classmethod
    def autoFormattingIndent(cls, self):
        'autoFormattingIndent(self) -> int'
        return 1
    
    @classmethod
    def codec(cls, self):
        'codec(self) -> QTextCodec'
        pass
    
    @classmethod
    def device(cls, self):
        'device(self) -> QIODevice'
        pass
    
    @classmethod
    def hasError(cls, self):
        'hasError(self) -> bool'
        return True
    
    @classmethod
    def setAutoFormatting(cls, self, bool):
        'setAutoFormatting(self, bool)'
        pass
    
    @classmethod
    def setAutoFormattingIndent(cls, self, int):
        'setAutoFormattingIndent(self, int)'
        pass
    
    @classmethod
    def setCodec(cls, self, QTextCodec):
        'setCodec(self, QTextCodec)\nsetCodec(self, str)'
        pass
    
    @classmethod
    def setDevice(cls, self, QIODevice):
        'setDevice(self, QIODevice)'
        pass
    
    @classmethod
    def writeAttribute(cls, self, QXmlStreamAttribute):
        'writeAttribute(self, str, str)\nwriteAttribute(self, str, str, str)\nwriteAttribute(self, QXmlStreamAttribute)'
        pass
    
    @classmethod
    def writeAttributes(cls, self, QXmlStreamAttributes):
        'writeAttributes(self, QXmlStreamAttributes)'
        pass
    
    @classmethod
    def writeCDATA(cls, self, str):
        'writeCDATA(self, str)'
        pass
    
    @classmethod
    def writeCharacters(cls, self, str):
        'writeCharacters(self, str)'
        pass
    
    @classmethod
    def writeComment(cls, self, str):
        'writeComment(self, str)'
        pass
    
    @classmethod
    def writeCurrentToken(cls, self, QXmlStreamReader):
        'writeCurrentToken(self, QXmlStreamReader)'
        pass
    
    @classmethod
    def writeDTD(cls, self, str):
        'writeDTD(self, str)'
        pass
    
    @classmethod
    def writeDefaultNamespace(cls, self, str):
        'writeDefaultNamespace(self, str)'
        pass
    
    @classmethod
    def writeEmptyElement(cls, self, str, str_):
        'writeEmptyElement(self, str)\nwriteEmptyElement(self, str, str)'
        pass
    
    @classmethod
    def writeEndDocument(cls, self):
        'writeEndDocument(self)'
        pass
    
    @classmethod
    def writeEndElement(cls, self):
        'writeEndElement(self)'
        pass
    
    @classmethod
    def writeEntityReference(cls, self, str):
        'writeEntityReference(self, str)'
        pass
    
    @classmethod
    def writeNamespace(cls, self, str, prefix: str=''):
        "writeNamespace(self, str, prefix: str = '')"
        pass
    
    @classmethod
    def writeProcessingInstruction(cls, self, str, data: str=''):
        "writeProcessingInstruction(self, str, data: str = '')"
        pass
    
    @classmethod
    def writeStartDocument(cls, self, str, bool):
        'writeStartDocument(self)\nwriteStartDocument(self, str)\nwriteStartDocument(self, str, bool)'
        pass
    
    @classmethod
    def writeStartElement(cls, self, str, str_):
        'writeStartElement(self, str)\nwriteStartElement(self, str, str)'
        pass
    
    @classmethod
    def writeTextElement(cls, self, str, str_, str_1):
        'writeTextElement(self, str, str)\nwriteTextElement(self, str, str, str)'
        pass
    

def Q_ARG(object, object_):
    'Q_ARG(object, object) -> QGenericArgument'
    pass

def Q_CLASSINFO(str, str_):
    'Q_CLASSINFO(str, str)'
    pass

def Q_ENUMS(*_):
    'Q_ENUMS(*)'
    pass

def Q_FLAGS(*_):
    'Q_FLAGS(*)'
    pass

def Q_RETURN_ARG(object):
    'Q_RETURN_ARG(object) -> QGenericReturnArgument'
    pass

class Qt(_mod_sip.simplewrapper):
    AA_CompressHighFrequencyEvents = ApplicationAttribute()
    AA_DisableHighDpiScaling = ApplicationAttribute()
    AA_DisableShaderDiskCache = ApplicationAttribute()
    AA_DontCheckOpenGLContextThreadAffinity = ApplicationAttribute()
    AA_DontCreateNativeWidgetSiblings = ApplicationAttribute()
    AA_DontShowIconsInMenus = ApplicationAttribute()
    AA_DontUseNativeDialogs = ApplicationAttribute()
    AA_DontUseNativeMenuBar = ApplicationAttribute()
    AA_EnableHighDpiScaling = ApplicationAttribute()
    AA_ForceRasterWidgets = ApplicationAttribute()
    AA_ImmediateWidgetCreation = ApplicationAttribute()
    AA_MSWindowsUseDirect3DByDefault = ApplicationAttribute()
    AA_MacDontSwapCtrlAndMeta = ApplicationAttribute()
    AA_MacPluginApplication = ApplicationAttribute()
    AA_NativeWindows = ApplicationAttribute()
    AA_PluginApplication = ApplicationAttribute()
    AA_SetPalette = ApplicationAttribute()
    AA_ShareOpenGLContexts = ApplicationAttribute()
    AA_SynthesizeMouseForUnhandledTabletEvents = ApplicationAttribute()
    AA_SynthesizeMouseForUnhandledTouchEvents = ApplicationAttribute()
    AA_SynthesizeTouchForUnhandledMouseEvents = ApplicationAttribute()
    AA_Use96Dpi = ApplicationAttribute()
    AA_UseDesktopOpenGL = ApplicationAttribute()
    AA_UseHighDpiPixmaps = ApplicationAttribute()
    AA_UseOpenGLES = ApplicationAttribute()
    AA_UseSoftwareOpenGL = ApplicationAttribute()
    AA_UseStyleSheetPropagationInWidgetStyles = ApplicationAttribute()
    AA_X11InitThreads = ApplicationAttribute()
    ALT = Modifier()
    AbsoluteSize = SizeMode()
    AccessibleDescriptionRole = ItemDataRole()
    AccessibleTextRole = ItemDataRole()
    ActionMask = DropAction()
    ActionsContextMenu = ContextMenuPolicy()
    ActiveWindowFocusReason = FocusReason()
    AddToSelection = ItemSelectionOperation()
    AlignAbsolute = AlignmentFlag()
    AlignBaseline = AlignmentFlag()
    AlignBottom = AlignmentFlag()
    AlignCenter = AlignmentFlag()
    AlignHCenter = AlignmentFlag()
    AlignHorizontal_Mask = AlignmentFlag()
    AlignJustify = AlignmentFlag()
    AlignLeading = AlignmentFlag()
    AlignLeft = AlignmentFlag()
    AlignRight = AlignmentFlag()
    AlignTop = AlignmentFlag()
    AlignTrailing = AlignmentFlag()
    AlignVCenter = AlignmentFlag()
    AlignVertical_Mask = AlignmentFlag()
    Alignment = Alignment
    AlignmentFlag = AlignmentFlag
    AllButtons = MouseButton()
    AllDockWidgetAreas = DockWidgetArea()
    AllToolBarAreas = ToolBarArea()
    AltModifier = KeyboardModifier()
    AnchorBottom = AnchorPoint()
    AnchorHorizontalCenter = AnchorPoint()
    AnchorLeft = AnchorPoint()
    AnchorPoint = AnchorPoint
    AnchorRight = AnchorPoint()
    AnchorTop = AnchorPoint()
    AnchorVerticalCenter = AnchorPoint()
    ApplicationActive = ApplicationState()
    ApplicationAttribute = ApplicationAttribute
    ApplicationHidden = ApplicationState()
    ApplicationInactive = ApplicationState()
    ApplicationModal = WindowModality()
    ApplicationShortcut = ShortcutContext()
    ApplicationState = ApplicationState
    ApplicationStates = ApplicationStates
    ApplicationSuspended = ApplicationState()
    ArrowCursor = CursorShape()
    ArrowType = ArrowType
    AscendingOrder = SortOrder()
    AspectRatioMode = AspectRatioMode
    AutoColor = ImageConversionFlag()
    AutoConnection = ConnectionType()
    AutoDither = ImageConversionFlag()
    AutoText = TextFormat()
    AvoidDither = ImageConversionFlag()
    Axis = Axis
    BDiagPattern = BrushStyle()
    BGMode = BGMode
    BackButton = MouseButton()
    BackgroundColorRole = ItemDataRole()
    BackgroundRole = ItemDataRole()
    BacktabFocusReason = FocusReason()
    BeginNativeGesture = NativeGestureType()
    BevelJoin = PenJoinStyle()
    BitmapCursor = CursorShape()
    BlankCursor = CursorShape()
    BlockingQueuedConnection = ConnectionType()
    BottomDockWidgetArea = DockWidgetArea()
    BottomEdge = Edge()
    BottomLeftCorner = Corner()
    BottomLeftSection = WindowFrameSection()
    BottomRightCorner = Corner()
    BottomRightSection = WindowFrameSection()
    BottomSection = WindowFrameSection()
    BottomToolBarArea = ToolBarArea()
    BrushStyle = BrushStyle
    BusyCursor = CursorShape()
    BypassGraphicsProxyWidget = WindowType()
    BypassWindowManagerHint = WindowType()
    CTRL = Modifier()
    CaseInsensitive = CaseSensitivity()
    CaseSensitive = CaseSensitivity()
    CaseSensitivity = CaseSensitivity
    CheckState = CheckState
    CheckStateRole = ItemDataRole()
    Checked = CheckState()
    ChecksumIso3309 = ChecksumType()
    ChecksumItuV41 = ChecksumType()
    ChecksumType = ChecksumType
    ClickFocus = FocusPolicy()
    ClipOperation = ClipOperation
    ClosedHandCursor = CursorShape()
    CoarseTimer = TimerType()
    ColorOnly = ImageConversionFlag()
    ConicalGradientPattern = BrushStyle()
    ConnectionType = ConnectionType
    ContainsItemBoundingRect = ItemSelectionMode()
    ContainsItemShape = ItemSelectionMode()
    ContextMenuPolicy = ContextMenuPolicy
    ControlModifier = KeyboardModifier()
    CoordinateSystem = CoordinateSystem
    CopyAction = DropAction()
    Corner = Corner
    CoverWindow = WindowType()
    CrossCursor = CursorShape()
    CrossPattern = BrushStyle()
    CursorMoveStyle = CursorMoveStyle
    CursorShape = CursorShape
    CustomContextMenu = ContextMenuPolicy()
    CustomCursor = CursorShape()
    CustomDashLine = PenStyle()
    CustomGesture = GestureType()
    CustomizeWindowHint = WindowType()
    DashDotDotLine = PenStyle()
    DashDotLine = PenStyle()
    DashLine = PenStyle()
    DateFormat = DateFormat
    DayOfWeek = DayOfWeek
    DecorationRole = ItemDataRole()
    DefaultContextMenu = ContextMenuPolicy()
    DefaultLocaleLongDate = DateFormat()
    DefaultLocaleShortDate = DateFormat()
    Dense1Pattern = BrushStyle()
    Dense2Pattern = BrushStyle()
    Dense3Pattern = BrushStyle()
    Dense4Pattern = BrushStyle()
    Dense5Pattern = BrushStyle()
    Dense6Pattern = BrushStyle()
    Dense7Pattern = BrushStyle()
    DescendingOrder = SortOrder()
    Desktop = WindowType()
    DeviceCoordinates = CoordinateSystem()
    DiagCrossPattern = BrushStyle()
    Dialog = WindowType()
    DiffuseAlphaDither = ImageConversionFlag()
    DiffuseDither = ImageConversionFlag()
    DirectConnection = ConnectionType()
    DisplayRole = ItemDataRole()
    DockWidgetArea = DockWidgetArea
    DockWidgetArea_Mask = DockWidgetArea()
    DockWidgetAreas = DockWidgetAreas
    DontStartGestureOnChildren = GestureFlag()
    DotLine = PenStyle()
    DownArrow = ArrowType()
    DragCopyCursor = CursorShape()
    DragLinkCursor = CursorShape()
    DragMoveCursor = CursorShape()
    Drawer = WindowType()
    DropAction = DropAction
    DropActions = DropActions
    Edge = Edge
    Edges = Edges
    EditRole = ItemDataRole()
    ElideLeft = TextElideMode()
    ElideMiddle = TextElideMode()
    ElideNone = TextElideMode()
    ElideRight = TextElideMode()
    EndNativeGesture = NativeGestureType()
    EnterKeyDefault = EnterKeyType()
    EnterKeyDone = EnterKeyType()
    EnterKeyGo = EnterKeyType()
    EnterKeyNext = EnterKeyType()
    EnterKeyPrevious = EnterKeyType()
    EnterKeyReturn = EnterKeyType()
    EnterKeySearch = EnterKeyType()
    EnterKeySend = EnterKeyType()
    EnterKeyType = EnterKeyType
    EventPriority = EventPriority
    ExactHit = HitTestAccuracy()
    ExtraButton1 = MouseButton()
    ExtraButton10 = MouseButton()
    ExtraButton11 = MouseButton()
    ExtraButton12 = MouseButton()
    ExtraButton13 = MouseButton()
    ExtraButton14 = MouseButton()
    ExtraButton15 = MouseButton()
    ExtraButton16 = MouseButton()
    ExtraButton17 = MouseButton()
    ExtraButton18 = MouseButton()
    ExtraButton19 = MouseButton()
    ExtraButton2 = MouseButton()
    ExtraButton20 = MouseButton()
    ExtraButton21 = MouseButton()
    ExtraButton22 = MouseButton()
    ExtraButton23 = MouseButton()
    ExtraButton24 = MouseButton()
    ExtraButton3 = MouseButton()
    ExtraButton4 = MouseButton()
    ExtraButton5 = MouseButton()
    ExtraButton6 = MouseButton()
    ExtraButton7 = MouseButton()
    ExtraButton8 = MouseButton()
    ExtraButton9 = MouseButton()
    FDiagPattern = BrushStyle()
    FastTransformation = TransformationMode()
    FillRule = FillRule
    FindChildOption = FindChildOption
    FindChildOptions = FindChildOptions
    FindChildrenRecursively = FindChildOption()
    FindDirectChildrenOnly = FindChildOption()
    FlatCap = PenCapStyle()
    FocusPolicy = FocusPolicy
    FocusReason = FocusReason
    FontRole = ItemDataRole()
    ForbiddenCursor = CursorShape()
    ForegroundRole = ItemDataRole()
    ForeignWindow = WindowType()
    ForwardButton = MouseButton()
    FramelessWindowHint = WindowType()
    Friday = DayOfWeek()
    FuzzyHit = HitTestAccuracy()
    GestureCanceled = GestureState()
    GestureFinished = GestureState()
    GestureFlag = GestureFlag
    GestureFlags = GestureFlags
    GestureStarted = GestureState()
    GestureState = GestureState
    GestureType = GestureType
    GestureUpdated = GestureState()
    GlobalColor = GlobalColor
    GroupSwitchModifier = KeyboardModifier()
    HighEventPriority = EventPriority()
    HitTestAccuracy = HitTestAccuracy
    HorPattern = BrushStyle()
    Horizontal = Orientation()
    IBeamCursor = CursorShape()
    ISODate = DateFormat()
    ISODateWithMs = DateFormat()
    IgnoreAction = DropAction()
    IgnoreAspectRatio = AspectRatioMode()
    IgnoredGesturesPropagateToParent = GestureFlag()
    ImAbsolutePosition = InputMethodQuery()
    ImAnchorPosition = InputMethodQuery()
    ImAnchorRectangle = InputMethodQuery()
    ImCurrentSelection = InputMethodQuery()
    ImCursorPosition = InputMethodQuery()
    ImCursorRectangle = InputMethodQuery()
    ImEnabled = InputMethodQuery()
    ImEnterKeyType = InputMethodQuery()
    ImFont = InputMethodQuery()
    ImHints = InputMethodQuery()
    ImInputItemClipRectangle = InputMethodQuery()
    ImMaximumTextLength = InputMethodQuery()
    ImMicroFocus = InputMethodQuery()
    ImPlatformData = InputMethodQuery()
    ImPreferredLanguage = InputMethodQuery()
    ImQueryAll = InputMethodQuery()
    ImQueryInput = InputMethodQuery()
    ImSurroundingText = InputMethodQuery()
    ImTextAfterCursor = InputMethodQuery()
    ImTextBeforeCursor = InputMethodQuery()
    ImageConversionFlag = ImageConversionFlag
    ImageConversionFlags = ImageConversionFlags
    ImhDate = InputMethodHint()
    ImhDialableCharactersOnly = InputMethodHint()
    ImhDigitsOnly = InputMethodHint()
    ImhEmailCharactersOnly = InputMethodHint()
    ImhExclusiveInputMask = InputMethodHint()
    ImhFormattedNumbersOnly = InputMethodHint()
    ImhHiddenText = InputMethodHint()
    ImhLatinOnly = InputMethodHint()
    ImhLowercaseOnly = InputMethodHint()
    ImhMultiLine = InputMethodHint()
    ImhNoAutoUppercase = InputMethodHint()
    ImhNoPredictiveText = InputMethodHint()
    ImhNone = InputMethodHint()
    ImhPreferLatin = InputMethodHint()
    ImhPreferLowercase = InputMethodHint()
    ImhPreferNumbers = InputMethodHint()
    ImhPreferUppercase = InputMethodHint()
    ImhSensitiveData = InputMethodHint()
    ImhTime = InputMethodHint()
    ImhUppercaseOnly = InputMethodHint()
    ImhUrlCharactersOnly = InputMethodHint()
    InitialSortOrderRole = ItemDataRole()
    InputMethodHint = InputMethodHint
    InputMethodHints = InputMethodHints
    InputMethodQueries = InputMethodQueries
    InputMethodQuery = InputMethodQuery
    IntersectClip = ClipOperation()
    IntersectsItemBoundingRect = ItemSelectionMode()
    IntersectsItemShape = ItemSelectionMode()
    InvertedLandscapeOrientation = ScreenOrientation()
    InvertedPortraitOrientation = ScreenOrientation()
    ItemDataRole = ItemDataRole
    ItemFlag = ItemFlag
    ItemFlags = ItemFlags
    ItemIsAutoTristate = ItemFlag()
    ItemIsDragEnabled = ItemFlag()
    ItemIsDropEnabled = ItemFlag()
    ItemIsEditable = ItemFlag()
    ItemIsEnabled = ItemFlag()
    ItemIsSelectable = ItemFlag()
    ItemIsTristate = ItemFlag()
    ItemIsUserCheckable = ItemFlag()
    ItemIsUserTristate = ItemFlag()
    ItemNeverHasChildren = ItemFlag()
    ItemSelectionMode = ItemSelectionMode
    ItemSelectionOperation = ItemSelectionOperation
    KeepAspectRatio = AspectRatioMode()
    KeepAspectRatioByExpanding = AspectRatioMode()
    Key = Key
    Key_0 = Key()
    Key_1 = Key()
    Key_2 = Key()
    Key_3 = Key()
    Key_4 = Key()
    Key_5 = Key()
    Key_6 = Key()
    Key_7 = Key()
    Key_8 = Key()
    Key_9 = Key()
    Key_A = Key()
    Key_AE = Key()
    Key_Aacute = Key()
    Key_Acircumflex = Key()
    Key_AddFavorite = Key()
    Key_Adiaeresis = Key()
    Key_Agrave = Key()
    Key_Alt = Key()
    Key_AltGr = Key()
    Key_Ampersand = Key()
    Key_Any = Key()
    Key_Apostrophe = Key()
    Key_ApplicationLeft = Key()
    Key_ApplicationRight = Key()
    Key_Aring = Key()
    Key_AsciiCircum = Key()
    Key_AsciiTilde = Key()
    Key_Asterisk = Key()
    Key_At = Key()
    Key_Atilde = Key()
    Key_AudioCycleTrack = Key()
    Key_AudioForward = Key()
    Key_AudioRandomPlay = Key()
    Key_AudioRepeat = Key()
    Key_AudioRewind = Key()
    Key_Away = Key()
    Key_B = Key()
    Key_Back = Key()
    Key_BackForward = Key()
    Key_Backslash = Key()
    Key_Backspace = Key()
    Key_Backtab = Key()
    Key_Bar = Key()
    Key_BassBoost = Key()
    Key_BassDown = Key()
    Key_BassUp = Key()
    Key_Battery = Key()
    Key_Blue = Key()
    Key_Bluetooth = Key()
    Key_Book = Key()
    Key_BraceLeft = Key()
    Key_BraceRight = Key()
    Key_BracketLeft = Key()
    Key_BracketRight = Key()
    Key_BrightnessAdjust = Key()
    Key_C = Key()
    Key_CD = Key()
    Key_Calculator = Key()
    Key_Calendar = Key()
    Key_Call = Key()
    Key_Camera = Key()
    Key_CameraFocus = Key()
    Key_Cancel = Key()
    Key_CapsLock = Key()
    Key_Ccedilla = Key()
    Key_ChannelDown = Key()
    Key_ChannelUp = Key()
    Key_Clear = Key()
    Key_ClearGrab = Key()
    Key_Close = Key()
    Key_Codeinput = Key()
    Key_Colon = Key()
    Key_Comma = Key()
    Key_Community = Key()
    Key_Context1 = Key()
    Key_Context2 = Key()
    Key_Context3 = Key()
    Key_Context4 = Key()
    Key_ContrastAdjust = Key()
    Key_Control = Key()
    Key_Copy = Key()
    Key_Cut = Key()
    Key_D = Key()
    Key_DOS = Key()
    Key_Dead_Abovedot = Key()
    Key_Dead_Abovering = Key()
    Key_Dead_Acute = Key()
    Key_Dead_Belowdot = Key()
    Key_Dead_Breve = Key()
    Key_Dead_Caron = Key()
    Key_Dead_Cedilla = Key()
    Key_Dead_Circumflex = Key()
    Key_Dead_Diaeresis = Key()
    Key_Dead_Doubleacute = Key()
    Key_Dead_Grave = Key()
    Key_Dead_Hook = Key()
    Key_Dead_Horn = Key()
    Key_Dead_Iota = Key()
    Key_Dead_Macron = Key()
    Key_Dead_Ogonek = Key()
    Key_Dead_Semivoiced_Sound = Key()
    Key_Dead_Tilde = Key()
    Key_Dead_Voiced_Sound = Key()
    Key_Delete = Key()
    Key_Direction_L = Key()
    Key_Direction_R = Key()
    Key_Display = Key()
    Key_Documents = Key()
    Key_Dollar = Key()
    Key_Down = Key()
    Key_E = Key()
    Key_ETH = Key()
    Key_Eacute = Key()
    Key_Ecircumflex = Key()
    Key_Ediaeresis = Key()
    Key_Egrave = Key()
    Key_Eisu_Shift = Key()
    Key_Eisu_toggle = Key()
    Key_Eject = Key()
    Key_End = Key()
    Key_Enter = Key()
    Key_Equal = Key()
    Key_Escape = Key()
    Key_Excel = Key()
    Key_Exclam = Key()
    Key_Execute = Key()
    Key_Exit = Key()
    Key_Explorer = Key()
    Key_F = Key()
    Key_F1 = Key()
    Key_F10 = Key()
    Key_F11 = Key()
    Key_F12 = Key()
    Key_F13 = Key()
    Key_F14 = Key()
    Key_F15 = Key()
    Key_F16 = Key()
    Key_F17 = Key()
    Key_F18 = Key()
    Key_F19 = Key()
    Key_F2 = Key()
    Key_F20 = Key()
    Key_F21 = Key()
    Key_F22 = Key()
    Key_F23 = Key()
    Key_F24 = Key()
    Key_F25 = Key()
    Key_F26 = Key()
    Key_F27 = Key()
    Key_F28 = Key()
    Key_F29 = Key()
    Key_F3 = Key()
    Key_F30 = Key()
    Key_F31 = Key()
    Key_F32 = Key()
    Key_F33 = Key()
    Key_F34 = Key()
    Key_F35 = Key()
    Key_F4 = Key()
    Key_F5 = Key()
    Key_F6 = Key()
    Key_F7 = Key()
    Key_F8 = Key()
    Key_F9 = Key()
    Key_Favorites = Key()
    Key_Finance = Key()
    Key_Find = Key()
    Key_Flip = Key()
    Key_Forward = Key()
    Key_G = Key()
    Key_Game = Key()
    Key_Go = Key()
    Key_Greater = Key()
    Key_Green = Key()
    Key_Guide = Key()
    Key_H = Key()
    Key_Hangul = Key()
    Key_Hangul_Banja = Key()
    Key_Hangul_End = Key()
    Key_Hangul_Hanja = Key()
    Key_Hangul_Jamo = Key()
    Key_Hangul_Jeonja = Key()
    Key_Hangul_PostHanja = Key()
    Key_Hangul_PreHanja = Key()
    Key_Hangul_Romaja = Key()
    Key_Hangul_Special = Key()
    Key_Hangul_Start = Key()
    Key_Hangup = Key()
    Key_Hankaku = Key()
    Key_Help = Key()
    Key_Henkan = Key()
    Key_Hibernate = Key()
    Key_Hiragana = Key()
    Key_Hiragana_Katakana = Key()
    Key_History = Key()
    Key_Home = Key()
    Key_HomePage = Key()
    Key_HotLinks = Key()
    Key_Hyper_L = Key()
    Key_Hyper_R = Key()
    Key_I = Key()
    Key_Iacute = Key()
    Key_Icircumflex = Key()
    Key_Idiaeresis = Key()
    Key_Igrave = Key()
    Key_Info = Key()
    Key_Insert = Key()
    Key_J = Key()
    Key_K = Key()
    Key_Kana_Lock = Key()
    Key_Kana_Shift = Key()
    Key_Kanji = Key()
    Key_Katakana = Key()
    Key_KeyboardBrightnessDown = Key()
    Key_KeyboardBrightnessUp = Key()
    Key_KeyboardLightOnOff = Key()
    Key_L = Key()
    Key_LastNumberRedial = Key()
    Key_Launch0 = Key()
    Key_Launch1 = Key()
    Key_Launch2 = Key()
    Key_Launch3 = Key()
    Key_Launch4 = Key()
    Key_Launch5 = Key()
    Key_Launch6 = Key()
    Key_Launch7 = Key()
    Key_Launch8 = Key()
    Key_Launch9 = Key()
    Key_LaunchA = Key()
    Key_LaunchB = Key()
    Key_LaunchC = Key()
    Key_LaunchD = Key()
    Key_LaunchE = Key()
    Key_LaunchF = Key()
    Key_LaunchG = Key()
    Key_LaunchH = Key()
    Key_LaunchMail = Key()
    Key_LaunchMedia = Key()
    Key_Left = Key()
    Key_Less = Key()
    Key_LightBulb = Key()
    Key_LogOff = Key()
    Key_M = Key()
    Key_MailForward = Key()
    Key_Market = Key()
    Key_Massyo = Key()
    Key_MediaLast = Key()
    Key_MediaNext = Key()
    Key_MediaPause = Key()
    Key_MediaPlay = Key()
    Key_MediaPrevious = Key()
    Key_MediaRecord = Key()
    Key_MediaStop = Key()
    Key_MediaTogglePlayPause = Key()
    Key_Meeting = Key()
    Key_Memo = Key()
    Key_Menu = Key()
    Key_MenuKB = Key()
    Key_MenuPB = Key()
    Key_Messenger = Key()
    Key_Meta = Key()
    Key_MicMute = Key()
    Key_MicVolumeDown = Key()
    Key_MicVolumeUp = Key()
    Key_Minus = Key()
    Key_Mode_switch = Key()
    Key_MonBrightnessDown = Key()
    Key_MonBrightnessUp = Key()
    Key_Muhenkan = Key()
    Key_Multi_key = Key()
    Key_MultipleCandidate = Key()
    Key_Music = Key()
    Key_MySites = Key()
    Key_N = Key()
    Key_New = Key()
    Key_News = Key()
    Key_No = Key()
    Key_Ntilde = Key()
    Key_NumLock = Key()
    Key_NumberSign = Key()
    Key_O = Key()
    Key_Oacute = Key()
    Key_Ocircumflex = Key()
    Key_Odiaeresis = Key()
    Key_OfficeHome = Key()
    Key_Ograve = Key()
    Key_Ooblique = Key()
    Key_Open = Key()
    Key_OpenUrl = Key()
    Key_Option = Key()
    Key_Otilde = Key()
    Key_P = Key()
    Key_PageDown = Key()
    Key_PageUp = Key()
    Key_ParenLeft = Key()
    Key_ParenRight = Key()
    Key_Paste = Key()
    Key_Pause = Key()
    Key_Percent = Key()
    Key_Period = Key()
    Key_Phone = Key()
    Key_Pictures = Key()
    Key_Play = Key()
    Key_Plus = Key()
    Key_PowerDown = Key()
    Key_PowerOff = Key()
    Key_PreviousCandidate = Key()
    Key_Print = Key()
    Key_Printer = Key()
    Key_Q = Key()
    Key_Question = Key()
    Key_QuoteDbl = Key()
    Key_QuoteLeft = Key()
    Key_R = Key()
    Key_Red = Key()
    Key_Redo = Key()
    Key_Refresh = Key()
    Key_Reload = Key()
    Key_Reply = Key()
    Key_Return = Key()
    Key_Right = Key()
    Key_Romaji = Key()
    Key_RotateWindows = Key()
    Key_RotationKB = Key()
    Key_RotationPB = Key()
    Key_S = Key()
    Key_Save = Key()
    Key_ScreenSaver = Key()
    Key_ScrollLock = Key()
    Key_Search = Key()
    Key_Select = Key()
    Key_Semicolon = Key()
    Key_Send = Key()
    Key_Settings = Key()
    Key_Shift = Key()
    Key_Shop = Key()
    Key_SingleCandidate = Key()
    Key_Slash = Key()
    Key_Sleep = Key()
    Key_Space = Key()
    Key_Spell = Key()
    Key_SplitScreen = Key()
    Key_Standby = Key()
    Key_Stop = Key()
    Key_Subtitle = Key()
    Key_Super_L = Key()
    Key_Super_R = Key()
    Key_Support = Key()
    Key_Suspend = Key()
    Key_SysReq = Key()
    Key_T = Key()
    Key_THORN = Key()
    Key_Tab = Key()
    Key_TaskPane = Key()
    Key_Terminal = Key()
    Key_Time = Key()
    Key_ToDoList = Key()
    Key_ToggleCallHangup = Key()
    Key_Tools = Key()
    Key_TopMenu = Key()
    Key_TouchpadOff = Key()
    Key_TouchpadOn = Key()
    Key_TouchpadToggle = Key()
    Key_Touroku = Key()
    Key_Travel = Key()
    Key_TrebleDown = Key()
    Key_TrebleUp = Key()
    Key_U = Key()
    Key_UWB = Key()
    Key_Uacute = Key()
    Key_Ucircumflex = Key()
    Key_Udiaeresis = Key()
    Key_Ugrave = Key()
    Key_Underscore = Key()
    Key_Undo = Key()
    Key_Up = Key()
    Key_V = Key()
    Key_Video = Key()
    Key_View = Key()
    Key_VoiceDial = Key()
    Key_VolumeDown = Key()
    Key_VolumeMute = Key()
    Key_VolumeUp = Key()
    Key_W = Key()
    Key_WLAN = Key()
    Key_WWW = Key()
    Key_WakeUp = Key()
    Key_WebCam = Key()
    Key_Word = Key()
    Key_X = Key()
    Key_Xfer = Key()
    Key_Y = Key()
    Key_Yacute = Key()
    Key_Yellow = Key()
    Key_Yes = Key()
    Key_Z = Key()
    Key_Zenkaku = Key()
    Key_Zenkaku_Hankaku = Key()
    Key_Zoom = Key()
    Key_ZoomIn = Key()
    Key_ZoomOut = Key()
    Key_acute = Key()
    Key_brokenbar = Key()
    Key_cedilla = Key()
    Key_cent = Key()
    Key_copyright = Key()
    Key_currency = Key()
    Key_degree = Key()
    Key_diaeresis = Key()
    Key_division = Key()
    Key_exclamdown = Key()
    Key_guillemotleft = Key()
    Key_guillemotright = Key()
    Key_hyphen = Key()
    Key_iTouch = Key()
    Key_macron = Key()
    Key_masculine = Key()
    Key_mu = Key()
    Key_multiply = Key()
    Key_nobreakspace = Key()
    Key_notsign = Key()
    Key_onehalf = Key()
    Key_onequarter = Key()
    Key_onesuperior = Key()
    Key_ordfeminine = Key()
    Key_paragraph = Key()
    Key_periodcentered = Key()
    Key_plusminus = Key()
    Key_questiondown = Key()
    Key_registered = Key()
    Key_section = Key()
    Key_ssharp = Key()
    Key_sterling = Key()
    Key_threequarters = Key()
    Key_threesuperior = Key()
    Key_twosuperior = Key()
    Key_unknown = Key()
    Key_ydiaeresis = Key()
    Key_yen = Key()
    KeyboardModifier = KeyboardModifier
    KeyboardModifierMask = KeyboardModifier()
    KeyboardModifiers = KeyboardModifiers
    KeypadModifier = KeyboardModifier()
    LandscapeOrientation = ScreenOrientation()
    LastCursor = CursorShape()
    LayoutDirection = LayoutDirection
    LayoutDirectionAuto = LayoutDirection()
    LeftArrow = ArrowType()
    LeftButton = MouseButton()
    LeftDockWidgetArea = DockWidgetArea()
    LeftEdge = Edge()
    LeftSection = WindowFrameSection()
    LeftToRight = LayoutDirection()
    LeftToolBarArea = ToolBarArea()
    LinearGradientPattern = BrushStyle()
    LinkAction = DropAction()
    LinksAccessibleByKeyboard = TextInteractionFlag()
    LinksAccessibleByMouse = TextInteractionFlag()
    LocalDate = DateFormat()
    LocalTime = TimeSpec()
    LocaleDate = DateFormat()
    LogicalCoordinates = CoordinateSystem()
    LogicalMoveStyle = CursorMoveStyle()
    LowEventPriority = EventPriority()
    META = Modifier()
    MODIFIER_MASK = Modifier()
    MPenCapStyle = PenCapStyle()
    MPenJoinStyle = PenJoinStyle()
    MPenStyle = PenStyle()
    MSWindowsFixedSizeDialogHint = WindowType()
    MSWindowsOwnDC = WindowType()
    MacWindowToolBarButtonHint = WindowType()
    MaskInColor = MaskMode()
    MaskMode = MaskMode
    MaskOutColor = MaskMode()
    MatchCaseSensitive = MatchFlag()
    MatchContains = MatchFlag()
    MatchEndsWith = MatchFlag()
    MatchExactly = MatchFlag()
    MatchFixedString = MatchFlag()
    MatchFlag = MatchFlag
    MatchFlags = MatchFlags
    MatchRecursive = MatchFlag()
    MatchRegExp = MatchFlag()
    MatchStartsWith = MatchFlag()
    MatchWildcard = MatchFlag()
    MatchWrap = MatchFlag()
    MaximizeUsingFullscreenGeometryHint = WindowType()
    MaximumSize = SizeHint()
    MenuBarFocusReason = FocusReason()
    MetaModifier = KeyboardModifier()
    MidButton = MouseButton()
    MiddleButton = MouseButton()
    MinimumDescent = SizeHint()
    MinimumSize = SizeHint()
    MiterJoin = PenJoinStyle()
    Modifier = Modifier
    Monday = DayOfWeek()
    MonoOnly = ImageConversionFlag()
    MouseButton = MouseButton
    MouseButtons = MouseButtons
    MouseEventCreatedDoubleClick = MouseEventFlag()
    MouseEventFlag = MouseEventFlag
    MouseEventFlags = MouseEventFlags
    MouseEventNotSynthesized = MouseEventSource()
    MouseEventSource = MouseEventSource
    MouseEventSynthesizedByApplication = MouseEventSource()
    MouseEventSynthesizedByQt = MouseEventSource()
    MouseEventSynthesizedBySystem = MouseEventSource()
    MouseFocusReason = FocusReason()
    MoveAction = DropAction()
    NativeGestureType = NativeGestureType
    NavigationMode = NavigationMode
    NavigationModeCursorAuto = NavigationMode()
    NavigationModeCursorForceVisible = NavigationMode()
    NavigationModeKeypadDirectional = NavigationMode()
    NavigationModeKeypadTabOrder = NavigationMode()
    NavigationModeNone = NavigationMode()
    NoArrow = ArrowType()
    NoBrush = BrushStyle()
    NoButton = MouseButton()
    NoClip = ClipOperation()
    NoContextMenu = ContextMenuPolicy()
    NoDockWidgetArea = DockWidgetArea()
    NoDropShadowWindowHint = WindowType()
    NoFocus = FocusPolicy()
    NoFocusReason = FocusReason()
    NoFormatConversion = ImageConversionFlag()
    NoItemFlags = ItemFlag()
    NoModifier = KeyboardModifier()
    NoOpaqueDetection = ImageConversionFlag()
    NoPen = PenStyle()
    NoScrollPhase = ScrollPhase()
    NoSection = WindowFrameSection()
    NoTabFocus = TabFocusBehavior()
    NoTextInteraction = TextInteractionFlag()
    NoToolBarArea = ToolBarArea()
    NonModal = WindowModality()
    NormalEventPriority = EventPriority()
    OddEvenFill = FillRule()
    OffsetFromUTC = TimeSpec()
    OpaqueMode = BGMode()
    OpenHandCursor = CursorShape()
    OrderedAlphaDither = ImageConversionFlag()
    OrderedDither = ImageConversionFlag()
    Orientation = Orientation
    Orientations = Orientations
    OtherFocusReason = FocusReason()
    PanGesture = GestureType()
    PanNativeGesture = NativeGestureType()
    PartiallyChecked = CheckState()
    PenCapStyle = PenCapStyle
    PenJoinStyle = PenJoinStyle
    PenStyle = PenStyle
    PinchGesture = GestureType()
    PlainText = TextFormat()
    PointingHandCursor = CursorShape()
    Popup = WindowType()
    PopupFocusReason = FocusReason()
    PortraitOrientation = ScreenOrientation()
    PreciseTimer = TimerType()
    PreferDither = ImageConversionFlag()
    PreferredSize = SizeHint()
    PreventContextMenu = ContextMenuPolicy()
    PrimaryOrientation = ScreenOrientation()
    QueuedConnection = ConnectionType()
    RFC2822Date = DateFormat()
    RadialGradientPattern = BrushStyle()
    ReceivePartialGestures = GestureFlag()
    RelativeSize = SizeMode()
    RepeatTile = TileRule()
    ReplaceClip = ClipOperation()
    ReplaceSelection = ItemSelectionOperation()
    RichText = TextFormat()
    RightArrow = ArrowType()
    RightButton = MouseButton()
    RightDockWidgetArea = DockWidgetArea()
    RightEdge = Edge()
    RightSection = WindowFrameSection()
    RightToLeft = LayoutDirection()
    RightToolBarArea = ToolBarArea()
    RotateNativeGesture = NativeGestureType()
    RoundCap = PenCapStyle()
    RoundJoin = PenJoinStyle()
    RoundTile = TileRule()
    SHIFT = Modifier()
    Saturday = DayOfWeek()
    ScreenOrientation = ScreenOrientation
    ScreenOrientations = ScreenOrientations
    ScrollBarAlwaysOff = ScrollBarPolicy()
    ScrollBarAlwaysOn = ScrollBarPolicy()
    ScrollBarAsNeeded = ScrollBarPolicy()
    ScrollBarPolicy = ScrollBarPolicy
    ScrollBegin = ScrollPhase()
    ScrollEnd = ScrollPhase()
    ScrollPhase = ScrollPhase
    ScrollUpdate = ScrollPhase()
    Sheet = WindowType()
    ShiftModifier = KeyboardModifier()
    ShortcutContext = ShortcutContext
    ShortcutFocusReason = FocusReason()
    SizeAllCursor = CursorShape()
    SizeBDiagCursor = CursorShape()
    SizeFDiagCursor = CursorShape()
    SizeHint = SizeHint
    SizeHintRole = ItemDataRole()
    SizeHorCursor = CursorShape()
    SizeMode = SizeMode
    SizeVerCursor = CursorShape()
    SmartZoomNativeGesture = NativeGestureType()
    SmoothTransformation = TransformationMode()
    SolidLine = PenStyle()
    SolidPattern = BrushStyle()
    SortOrder = SortOrder
    SplashScreen = WindowType()
    SplitHCursor = CursorShape()
    SplitVCursor = CursorShape()
    SquareCap = PenCapStyle()
    StatusTipRole = ItemDataRole()
    StretchTile = TileRule()
    StrongFocus = FocusPolicy()
    SubWindow = WindowType()
    Sunday = DayOfWeek()
    SvgMiterJoin = PenJoinStyle()
    SwipeGesture = GestureType()
    SwipeNativeGesture = NativeGestureType()
    SystemLocaleDate = DateFormat()
    SystemLocaleLongDate = DateFormat()
    SystemLocaleShortDate = DateFormat()
    TabFocus = FocusPolicy()
    TabFocusAllControls = TabFocusBehavior()
    TabFocusBehavior = TabFocusBehavior
    TabFocusListControls = TabFocusBehavior()
    TabFocusReason = FocusReason()
    TabFocusTextControls = TabFocusBehavior()
    TapAndHoldGesture = GestureType()
    TapGesture = GestureType()
    TargetMoveAction = DropAction()
    TaskButton = MouseButton()
    TextAlignmentRole = ItemDataRole()
    TextBrowserInteraction = TextInteractionFlag()
    TextColorRole = ItemDataRole()
    TextDate = DateFormat()
    TextDontClip = TextFlag()
    TextDontPrint = TextFlag()
    TextEditable = TextInteractionFlag()
    TextEditorInteraction = TextInteractionFlag()
    TextElideMode = TextElideMode
    TextExpandTabs = TextFlag()
    TextFlag = TextFlag
    TextFormat = TextFormat
    TextHideMnemonic = TextFlag()
    TextIncludeTrailingSpaces = TextFlag()
    TextInteractionFlag = TextInteractionFlag
    TextInteractionFlags = TextInteractionFlags
    TextJustificationForced = TextFlag()
    TextSelectableByKeyboard = TextInteractionFlag()
    TextSelectableByMouse = TextInteractionFlag()
    TextShowMnemonic = TextFlag()
    TextSingleLine = TextFlag()
    TextWordWrap = TextFlag()
    TextWrapAnywhere = TextFlag()
    TexturePattern = BrushStyle()
    ThresholdAlphaDither = ImageConversionFlag()
    ThresholdDither = ImageConversionFlag()
    Thursday = DayOfWeek()
    TileRule = TileRule
    TimeSpec = TimeSpec
    TimeZone = TimeSpec()
    TimerType = TimerType
    TitleBarArea = WindowFrameSection()
    Tool = WindowType()
    ToolBarArea = ToolBarArea
    ToolBarArea_Mask = ToolBarArea()
    ToolBarAreas = ToolBarAreas
    ToolButtonFollowStyle = ToolButtonStyle()
    ToolButtonIconOnly = ToolButtonStyle()
    ToolButtonStyle = ToolButtonStyle
    ToolButtonTextBesideIcon = ToolButtonStyle()
    ToolButtonTextOnly = ToolButtonStyle()
    ToolButtonTextUnderIcon = ToolButtonStyle()
    ToolTip = WindowType()
    ToolTipRole = ItemDataRole()
    TopDockWidgetArea = DockWidgetArea()
    TopEdge = Edge()
    TopLeftCorner = Corner()
    TopLeftSection = WindowFrameSection()
    TopRightCorner = Corner()
    TopRightSection = WindowFrameSection()
    TopSection = WindowFrameSection()
    TopToolBarArea = ToolBarArea()
    TouchPointMoved = TouchPointState()
    TouchPointPressed = TouchPointState()
    TouchPointReleased = TouchPointState()
    TouchPointState = TouchPointState
    TouchPointStates = TouchPointStates
    TouchPointStationary = TouchPointState()
    TransformationMode = TransformationMode
    TransparentMode = BGMode()
    Tuesday = DayOfWeek()
    UIEffect = UIEffect
    UI_AnimateCombo = UIEffect()
    UI_AnimateMenu = UIEffect()
    UI_AnimateToolBox = UIEffect()
    UI_AnimateTooltip = UIEffect()
    UI_FadeMenu = UIEffect()
    UI_FadeTooltip = UIEffect()
    UI_General = UIEffect()
    UNICODE_ACCEL = Modifier()
    UTC = TimeSpec()
    Unchecked = CheckState()
    UniqueConnection = ConnectionType()
    UpArrow = ArrowType()
    UpArrowCursor = CursorShape()
    UserRole = ItemDataRole()
    VerPattern = BrushStyle()
    Vertical = Orientation()
    VeryCoarseTimer = TimerType()
    VisualMoveStyle = CursorMoveStyle()
    WA_AcceptDrops = WidgetAttribute()
    WA_AcceptTouchEvents = WidgetAttribute()
    WA_AlwaysShowToolTips = WidgetAttribute()
    WA_AlwaysStackOnTop = WidgetAttribute()
    WA_AttributeCount = WidgetAttribute()
    WA_CustomWhatsThis = WidgetAttribute()
    WA_DeleteOnClose = WidgetAttribute()
    WA_Disabled = WidgetAttribute()
    WA_DontCreateNativeAncestors = WidgetAttribute()
    WA_DontShowOnScreen = WidgetAttribute()
    WA_ForceDisabled = WidgetAttribute()
    WA_ForceUpdatesDisabled = WidgetAttribute()
    WA_GrabbedShortcut = WidgetAttribute()
    WA_GroupLeader = WidgetAttribute()
    WA_Hover = WidgetAttribute()
    WA_InputMethodEnabled = WidgetAttribute()
    WA_InputMethodTransparent = WidgetAttribute()
    WA_InvalidSize = WidgetAttribute()
    WA_KeyCompression = WidgetAttribute()
    WA_KeyboardFocusChange = WidgetAttribute()
    WA_LaidOut = WidgetAttribute()
    WA_LayoutOnEntireRect = WidgetAttribute()
    WA_LayoutUsesWidgetRect = WidgetAttribute()
    WA_MSWindowsUseDirect3D = WidgetAttribute()
    WA_MacAlwaysShowToolWindow = WidgetAttribute()
    WA_MacBrushedMetal = WidgetAttribute()
    WA_MacFrameworkScaled = WidgetAttribute()
    WA_MacMetalStyle = WidgetAttribute()
    WA_MacMiniSize = WidgetAttribute()
    WA_MacNoClickThrough = WidgetAttribute()
    WA_MacNoShadow = WidgetAttribute()
    WA_MacNormalSize = WidgetAttribute()
    WA_MacOpaqueSizeGrip = WidgetAttribute()
    WA_MacShowFocusRect = WidgetAttribute()
    WA_MacSmallSize = WidgetAttribute()
    WA_MacVariableSize = WidgetAttribute()
    WA_Mapped = WidgetAttribute()
    WA_MouseNoMask = WidgetAttribute()
    WA_MouseTracking = WidgetAttribute()
    WA_Moved = WidgetAttribute()
    WA_NativeWindow = WidgetAttribute()
    WA_NoChildEventsForParent = WidgetAttribute()
    WA_NoChildEventsFromChildren = WidgetAttribute()
    WA_NoMousePropagation = WidgetAttribute()
    WA_NoMouseReplay = WidgetAttribute()
    WA_NoSystemBackground = WidgetAttribute()
    WA_NoX11EventCompression = WidgetAttribute()
    WA_OpaquePaintEvent = WidgetAttribute()
    WA_OutsideWSRange = WidgetAttribute()
    WA_PaintOnScreen = WidgetAttribute()
    WA_PaintUnclipped = WidgetAttribute()
    WA_PendingMoveEvent = WidgetAttribute()
    WA_PendingResizeEvent = WidgetAttribute()
    WA_PendingUpdate = WidgetAttribute()
    WA_QuitOnClose = WidgetAttribute()
    WA_Resized = WidgetAttribute()
    WA_RightToLeft = WidgetAttribute()
    WA_SetCursor = WidgetAttribute()
    WA_SetFont = WidgetAttribute()
    WA_SetLayoutDirection = WidgetAttribute()
    WA_SetLocale = WidgetAttribute()
    WA_SetPalette = WidgetAttribute()
    WA_SetStyle = WidgetAttribute()
    WA_SetWindowIcon = WidgetAttribute()
    WA_ShowWithoutActivating = WidgetAttribute()
    WA_StaticContents = WidgetAttribute()
    WA_StyleSheet = WidgetAttribute()
    WA_StyledBackground = WidgetAttribute()
    WA_TabletTracking = WidgetAttribute()
    WA_TintedBackground = WidgetAttribute()
    WA_TouchPadAcceptSingleTouchEvents = WidgetAttribute()
    WA_TranslucentBackground = WidgetAttribute()
    WA_TransparentForMouseEvents = WidgetAttribute()
    WA_UnderMouse = WidgetAttribute()
    WA_UpdatesDisabled = WidgetAttribute()
    WA_WState_CompressKeys = WidgetAttribute()
    WA_WState_ConfigPending = WidgetAttribute()
    WA_WState_Created = WidgetAttribute()
    WA_WState_ExplicitShowHide = WidgetAttribute()
    WA_WState_Hidden = WidgetAttribute()
    WA_WState_InPaintEvent = WidgetAttribute()
    WA_WState_OwnSizePolicy = WidgetAttribute()
    WA_WState_Polished = WidgetAttribute()
    WA_WState_Reparented = WidgetAttribute()
    WA_WState_Visible = WidgetAttribute()
    WA_WindowModified = WidgetAttribute()
    WA_WindowPropagation = WidgetAttribute()
    WA_X11DoNotAcceptFocus = WidgetAttribute()
    WA_X11NetWmWindowTypeCombo = WidgetAttribute()
    WA_X11NetWmWindowTypeDND = WidgetAttribute()
    WA_X11NetWmWindowTypeDesktop = WidgetAttribute()
    WA_X11NetWmWindowTypeDialog = WidgetAttribute()
    WA_X11NetWmWindowTypeDock = WidgetAttribute()
    WA_X11NetWmWindowTypeDropDownMenu = WidgetAttribute()
    WA_X11NetWmWindowTypeMenu = WidgetAttribute()
    WA_X11NetWmWindowTypeNotification = WidgetAttribute()
    WA_X11NetWmWindowTypePopupMenu = WidgetAttribute()
    WA_X11NetWmWindowTypeSplash = WidgetAttribute()
    WA_X11NetWmWindowTypeToolBar = WidgetAttribute()
    WA_X11NetWmWindowTypeToolTip = WidgetAttribute()
    WA_X11NetWmWindowTypeUtility = WidgetAttribute()
    WA_X11OpenGLOverlay = WidgetAttribute()
    WaitCursor = CursorShape()
    Wednesday = DayOfWeek()
    WhatsThisCursor = CursorShape()
    WhatsThisRole = ItemDataRole()
    WheelFocus = FocusPolicy()
    WhiteSpaceMode = WhiteSpaceMode
    WhiteSpaceModeUndefined = WhiteSpaceMode()
    WhiteSpaceNoWrap = WhiteSpaceMode()
    WhiteSpaceNormal = WhiteSpaceMode()
    WhiteSpacePre = WhiteSpaceMode()
    Widget = WindowType()
    WidgetAttribute = WidgetAttribute
    WidgetShortcut = ShortcutContext()
    WidgetWithChildrenShortcut = ShortcutContext()
    WindingFill = FillRule()
    Window = WindowType()
    WindowActive = WindowState()
    WindowCloseButtonHint = WindowType()
    WindowContextHelpButtonHint = WindowType()
    WindowDoesNotAcceptFocus = WindowType()
    WindowFlags = WindowFlags
    WindowFrameSection = WindowFrameSection
    WindowFullScreen = WindowState()
    WindowFullscreenButtonHint = WindowType()
    WindowMaximizeButtonHint = WindowType()
    WindowMaximized = WindowState()
    WindowMinMaxButtonsHint = WindowType()
    WindowMinimizeButtonHint = WindowType()
    WindowMinimized = WindowState()
    WindowModal = WindowModality()
    WindowModality = WindowModality
    WindowNoState = WindowState()
    WindowOverridesSystemGestures = WindowType()
    WindowShadeButtonHint = WindowType()
    WindowShortcut = ShortcutContext()
    WindowState = WindowState
    WindowStates = WindowStates
    WindowStaysOnBottomHint = WindowType()
    WindowStaysOnTopHint = WindowType()
    WindowSystemMenuHint = WindowType()
    WindowTitleHint = WindowType()
    WindowTransparentForInput = WindowType()
    WindowType = WindowType
    WindowType_Mask = WindowType()
    X11BypassWindowManagerHint = WindowType()
    XAxis = Axis()
    XButton1 = MouseButton()
    XButton2 = MouseButton()
    YAxis = Axis()
    ZAxis = Axis()
    ZoomNativeGesture = NativeGestureType()
    __class__ = Qt
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @property
    def __weakref__(self):
        'list of weak references to the object (if defined)'
        pass
    
    black = GlobalColor()
    blue = GlobalColor()
    color0 = GlobalColor()
    color1 = GlobalColor()
    cyan = GlobalColor()
    darkBlue = GlobalColor()
    darkCyan = GlobalColor()
    darkGray = GlobalColor()
    darkGreen = GlobalColor()
    darkMagenta = GlobalColor()
    darkRed = GlobalColor()
    darkYellow = GlobalColor()
    gray = GlobalColor()
    green = GlobalColor()
    lightGray = GlobalColor()
    magenta = GlobalColor()
    red = GlobalColor()
    transparent = GlobalColor()
    white = GlobalColor()
    yellow = GlobalColor()

QtCriticalMsg = QtMsgType()
QtDebugMsg = QtMsgType()
QtFatalMsg = QtMsgType()
QtInfoMsg = QtMsgType()
class QtMsgType(_mod_builtins.int):
    __class__ = QtMsgType
    __dict__ = {}
    def __init__(self, *args, **kwargs):
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    @classmethod
    def from_bytes(cls, type, bytes, byteorder):
        "Return the integer represented by the given array of bytes.\n\n  bytes\n    Holds the array of bytes to convert.  The argument must either\n    support the buffer protocol or be an iterable object producing bytes.\n    Bytes and bytearray are examples of built-in objects that support the\n    buffer protocol.\n  byteorder\n    The byte order used to represent the integer.  If byteorder is 'big',\n    the most significant byte is at the beginning of the byte array.  If\n    byteorder is 'little', the most significant byte is at the end of the\n    byte array.  To request the native byte order of the host system, use\n    `sys.byteorder' as the byte order value.\n  signed\n    Indicates whether two's complement is used to represent the integer."
        pass
    

QtSystemMsg = QtMsgType()
QtWarningMsg = QtMsgType()
__doc__ = None
__file__ = 'c:\\users\\twedw\\anaconda3\\lib\\site-packages\\PyQt5\\QtCore.pyd'
__license__ = _mod_builtins.mappingproxy()
__name__ = 'PyQt5.QtCore'
__package__ = 'PyQt5'
def bin_(QTextStream):
    'bin_(QTextStream) -> QTextStream'
    pass

def bom(QTextStream):
    'bom(QTextStream) -> QTextStream'
    pass

def center(QTextStream):
    'center(QTextStream) -> QTextStream'
    pass

def dec(QTextStream):
    'dec(QTextStream) -> QTextStream'
    pass

def endl(QTextStream):
    'endl(QTextStream) -> QTextStream'
    pass

def fixed(QTextStream):
    'fixed(QTextStream) -> QTextStream'
    pass

def flush(QTextStream):
    'flush(QTextStream) -> QTextStream'
    pass

def forcepoint(QTextStream):
    'forcepoint(QTextStream) -> QTextStream'
    pass

def forcesign(QTextStream):
    'forcesign(QTextStream) -> QTextStream'
    pass

def hex_(QTextStream):
    'hex_(QTextStream) -> QTextStream'
    pass

def left(QTextStream):
    'left(QTextStream) -> QTextStream'
    pass

def lowercasebase(QTextStream):
    'lowercasebase(QTextStream) -> QTextStream'
    pass

def lowercasedigits(QTextStream):
    'lowercasedigits(QTextStream) -> QTextStream'
    pass

def noforcepoint(QTextStream):
    'noforcepoint(QTextStream) -> QTextStream'
    pass

def noforcesign(QTextStream):
    'noforcesign(QTextStream) -> QTextStream'
    pass

def noshowbase(QTextStream):
    'noshowbase(QTextStream) -> QTextStream'
    pass

def oct_(QTextStream):
    'oct_(QTextStream) -> QTextStream'
    pass

class pyqtBoundSignal(_mod_builtins.object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = pyqtBoundSignal
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def connect(self, slot, type=Qt.AutoConnection, no_receiver_check=False):
        "connect(slot, type=Qt.AutoConnection, no_receiver_check=False)\n\nslot is either a Python callable or another signal.\ntype is a Qt.ConnectionType.\nno_receiver_check is True to disable the check that the receiver's C++\ninstance still exists when the signal is emitted.\n"
        pass
    
    def disconnect(self, slot=None):
        'disconnect([slot])\n\nslot is an optional Python callable or another signal.  If it is omitted\nthen the signal is disconnected from everything it is connected to.'
        pass
    
    def emit(self, *args):
        'emit(*args)\n\n*args are the values that will be passed as arguments to all connected\nslots.'
        pass
    
    @property
    def signal(self):
        'The signature of the signal that would be returned by SIGNAL()'
        pass
    

def pyqtPickleProtocol():
    'pyqtPickleProtocol() -> Optional[int]'
    pass

class pyqtProperty(_mod_builtins.object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = pyqtProperty
    def __delete__(self, instance):
        'Delete an attribute of instance.'
        pass
    
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return pyqtProperty()
    
    def __getattribute__(self, name):
        'Return getattr(self, name).'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    def __set__(self, instance, value):
        'Set an attribute of instance to value.'
        return None
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    
    def deleter(self):
        'Descriptor to change the deleter on a property.'
        pass
    
    @property
    def fdel(self):
        pass
    
    @property
    def fget(self):
        pass
    
    @property
    def freset(self):
        pass
    
    @property
    def fset(self):
        pass
    
    def getter(self):
        'Descriptor to change the getter on a property.'
        pass
    
    def read(self):
        'Descriptor to change the getter on a property.'
        pass
    
    def reset(self):
        'Descriptor to change the reset on a property.'
        pass
    
    def setter(self):
        'Descriptor to change the setter on a property.'
        pass
    
    @property
    def type(self):
        pass
    
    def write(self):
        'Descriptor to change the setter on a property.'
        pass
    

def pyqtRemoveInputHook():
    'pyqtRemoveInputHook()'
    pass

def pyqtRestoreInputHook():
    'pyqtRestoreInputHook()'
    pass

def pyqtSetPickleProtocol(Optionalint=None):
    'pyqtSetPickleProtocol(Optional[int])'
    pass

class pyqtSignal(_mod_builtins.object):
    def __call__(self, *args, **kwargs):
        'Call self as a function.'
        pass
    
    __class__ = pyqtSignal
    def __get__(self, instance, owner):
        'Return an attribute of instance, which is of type owner.'
        return pyqtSignal()
    
    def __getitem__(self, key):
        'Return self[key].'
        pass
    
    @classmethod
    def __init_subclass__(cls):
        'This method is called when a class is subclassed.\n\nThe default implementation does nothing. It may be\noverridden to extend subclasses.\n'
        return None
    
    __module__ = 'PyQt5.QtCore'
    def __repr__(self):
        'Return repr(self).'
        return ''
    
    @classmethod
    def __subclasshook__(cls, subclass):
        'Abstract classes can override this to customize issubclass().\n\nThis is invoked early on by abc.ABCMeta.__subclasscheck__().\nIt should return True, False or NotImplemented.  If it returns\nNotImplemented, the normal algorithm is used.  Otherwise, it\noverrides the normal algorithm (and the outcome is cached).\n'
        return False
    

def pyqtSlot(*types, name: Optional[str]=None, result: Optional[str]=None):
    '@pyqtSlot(*types, name: Optional[str], result: Optional[str])\n\nThis is a decorator applied to Python methods of a QObject that marks them\nas Qt slots.\nThe non-keyword arguments are the types of the slot arguments and each may\nbe a Python type object or a string specifying a C++ type.\nname is the name of the slot and defaults to the name of the method.\nresult is type of the value returned by the slot.'
    pass

def qAbs(float):
    'qAbs(float) -> float'
    return 1.0

def qAddPostRoutine():
    'qAddPostRoutine(Callable[..., None])'
    pass

def qAddPreRoutine(Callable, None_):
    'qAddPreRoutine(Callable[[], None])'
    pass

def qChecksum(bytes, QtChecksumType):
    'qChecksum(bytes) -> int\nqChecksum(bytes, Qt.ChecksumType) -> int'
    return 1

def qCompress(UnionQByteArray=None, bytes=None, bytearray=None, compressionLevel: int=-1):
    'qCompress(Union[QByteArray, bytes, bytearray], compressionLevel: int = -1) -> QByteArray'
    pass

def qCritical(str):
    'qCritical(str)'
    pass

def qDebug(str):
    'qDebug(str)'
    pass

def qErrnoWarning(int, str):
    'qErrnoWarning(int, str)\nqErrnoWarning(str)'
    pass

def qFatal(str):
    'qFatal(str)'
    pass

def qFloatDistance(float, float_):
    'qFloatDistance(float, float) -> int'
    return 1

def qFormatLogMessage(QtMsgType, QMessageLogContext, str):
    'qFormatLogMessage(QtMsgType, QMessageLogContext, str) -> str'
    return ''

def qFuzzyCompare(float, float_):
    'qFuzzyCompare(float, float) -> bool'
    return True

def qInf():
    'qInf() -> float'
    return 1.0

def qInstallMessageHandler(OptionalCallable=None, None_=None):
    'qInstallMessageHandler(Optional[Callable[[], None]]) -> Optional[Callable[[], None]]'
    pass

def qIsFinite(float):
    'qIsFinite(float) -> bool'
    return True

def qIsInf(float):
    'qIsInf(float) -> bool'
    return True

def qIsNaN(float):
    'qIsNaN(float) -> bool'
    return True

def qIsNull(float):
    'qIsNull(float) -> bool'
    return True

def qQNaN():
    'qQNaN() -> float'
    return 1.0

def qRegisterResourceData(int, bytes, bytes_, bytes_1):
    'qRegisterResourceData(int, bytes, bytes, bytes) -> bool'
    return True

def qRemovePostRoutine():
    'qRemovePostRoutine(Callable[..., None])'
    pass

def qRound(float):
    'qRound(float) -> int'
    return 1

def qRound64(float):
    'qRound64(float) -> int'
    return 1

def qSNaN():
    'qSNaN() -> float'
    return 1.0

def qSetFieldWidth(int):
    'qSetFieldWidth(int) -> QTextStreamManipulator'
    pass

def qSetMessagePattern(str):
    'qSetMessagePattern(str)'
    pass

def qSetPadChar(str):
    'qSetPadChar(str) -> QTextStreamManipulator'
    pass

def qSetRealNumberPrecision(int):
    'qSetRealNumberPrecision(int) -> QTextStreamManipulator'
    pass

def qSharedBuild():
    'qSharedBuild() -> bool'
    return True

def qUncompress(UnionQByteArray=None, bytes=None, bytearray=None):
    'qUncompress(Union[QByteArray, bytes, bytearray]) -> QByteArray'
    pass

def qUnregisterResourceData(int, bytes, bytes_, bytes_1):
    'qUnregisterResourceData(int, bytes, bytes, bytes) -> bool'
    return True

def qVersion():
    'qVersion() -> str'
    return ''

def qWarning(str):
    'qWarning(str)'
    pass

def qrand():
    'qrand() -> int'
    return 1

def qsrand(int):
    'qsrand(int)'
    pass

def reset(QTextStream):
    'reset(QTextStream) -> QTextStream'
    pass

def right(QTextStream):
    'right(QTextStream) -> QTextStream'
    pass

def scientific(QTextStream):
    'scientific(QTextStream) -> QTextStream'
    pass

def showbase(QTextStream):
    'showbase(QTextStream) -> QTextStream'
    pass

def uppercasebase(QTextStream):
    'uppercasebase(QTextStream) -> QTextStream'
    pass

def uppercasedigits(QTextStream):
    'uppercasedigits(QTextStream) -> QTextStream'
    pass

def ws(QTextStream):
    'ws(QTextStream) -> QTextStream'
    pass

