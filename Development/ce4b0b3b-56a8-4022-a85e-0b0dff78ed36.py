
class CachedLimiterSession(CacheMixin, LimiterMixin, Session):
    pass
session = CachedLimiterSession(
    limiter=Limiter(RequestRate(2, Duration.SECOND*50)),  # max 2 requests per 50 seconds
    bucket_class=MemoryQueueBucket,
    backend=SQLiteCache("yfinance.cache"),
) 