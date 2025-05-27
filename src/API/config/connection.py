from clickhouse_driver import Client as ClickHouseClient
from supabase import create_client, Client as SupabaseClient
from config import settings

class DatabaseConnection:
    _instance = None
    _client = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseConnection, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._client is None:
            self._client = ClickHouseClient(
                host=settings.CLICKHOUSE_HOST,
                user=settings.CLICKHOUSE_USER,
                password=settings.CLICKHOUSE_PASSWORD,
                secure=True
            )

    @property
    def client(self):
        return self._client

    def execute_query(self, query: str, with_column_types: bool = True):
        """
        Executa uma query no ClickHouse
        
        Args:
            query (str): Query SQL a ser executada
            with_column_types (bool): Se deve retornar informações sobre as colunas
            
        Returns:
            tuple: (dados, tipos_colunas) se with_column_types=True, senão apenas dados
        """
        return self._client.execute(query, with_column_types=with_column_types) 

supabase: SupabaseClient = create_client(
    settings.SUPABASE_URL,
    settings.SUPABASE_API_KEY
)


