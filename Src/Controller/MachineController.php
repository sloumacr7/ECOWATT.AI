<?php

namespace App\Controller;

use Symfony\Bundle\FrameworkBundle\Controller\AbstractController;
use Symfony\Component\HttpFoundation\Response;
use Symfony\Component\Routing\Annotation\Route;

class MachineController extends AbstractController
{
    #[Route('/dashboard1', name: 'dashboard1')]
    public function index(): Response
    {
        // Exemple de données fictives
        $data = [
            'voltage' => [220, 221, 219, 222, 220],
            'energy' => [0.01, 0.02, 0.015, 0.02, 0.01],
            'frequency' => [49.5, 49.6, 49.4, 49.7, 49.3],
            'amperage' => [3.1, 3.2, 3.25, 3.3, 3.1],
            'alarms' => [
                [
                    'time' => '2024-11-18 14:27:29',
                    'type' => 'Low Voltage Alarm',
                    'severity' => 'Critical',
                    'status' => 'Active Unacknowledged',
                ],
            ],
        ];

        return $this->render('machine/index.html.twig', ['data' => $data]);
    }
}
