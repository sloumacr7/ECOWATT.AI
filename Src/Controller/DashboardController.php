<?php
namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class DashboardController extends AbstractController
{
    #[Route('/dashboard', name: 'dash')]
    public function index(): Response
    {
        // Mock data (replace with real data from your database)
        $stats = [
            'locations' => 45,
            'onlineDevices' => 17,
            'offlineDevices' => 2,
            'deployedDevices' => 9,
        ];

        $consumptionData = [
            'thisWeek' => 1917.4,
            'lastWeek' => 1920,
        ];

        $costData = [
            'thisWeek' => 85,
            'lastWeek' => 73,
        ];

        $emissions = [
            'thisWeek' => 94,
            'lastWeek' => 88,
        ];

        $graphData = [
            'labels' => ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday'],
            'consumption' => [100, 200, 150, 250, 300],
            'cost' => [10, 20, 15, 25, 30],
        ];

        $events = [
            ['status' => 'Stopped', 'date' => '2022-03-11 11:03:19', 'description' => 'TR2 issue in data transmission.'],
            ['status' => 'Pending', 'date' => '2022-03-11 11:03:19', 'description' => 'TR2 pending data resolution.'],
        ];

        return $this->render('dashboard/index.html.twig', [
            'stats' => $stats,
            'consumptionData' => $consumptionData,
            'costData' => $costData,
            'emissions' => $emissions,
            'graphData' => $graphData,
            'events' => $events,
        ]);
    }
}
